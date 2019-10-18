import requests
import boto3
import io
import PIL.Image
import os

s3 = boto3.client('s3')
thumbnailSize = int(os.environ['THUMBNAIL_SIZE'])


def createThumbnail(event, context):
    """
    Executed by an S3 trigger create file event
    """
    # Debug purposed print
    #print("event:", event, "context:", context)
    
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        s3ObjectKey = event['Records'][0]['s3']['object']['key']

        if bucket is not None:
            print(f"Bucket: {bucket}") 

        if s3ObjectKey is not None:
            print(f"S3object: {s3ObjectKey}")
    except Exception as e:
        print(e)
        return("General error")

    # don't create thumbnail for a file that is already a thumbnail
    #  => especially because the function fires off againwhen thumbnail is created
    if "thumbnail" in s3ObjectKey:
        print(f"Function called on a file that is thumbnail already: {s3ObjectKey}")
        return None

    # retrieve image binary representation
    img = getS3Image(bucket,s3ObjectKey)
    print(img.size)

    # produce image's thumbnail
    imgThumbnail = getImageThumbnail(img)
    print(imgThumbnail.size)

    # compose thumbnail's name
    thumbnailFileName = newFilename(s3ObjectKey)
    print(f"Thumbnail filename: {thumbnailFileName}")

    # upload thumbnail to s3
    thumbnailUrl = uploadToS3(bucket,thumbnailFileName,imgThumbnail)

    print(f"Thumbnail url: {thumbnailUrl}")
    return thumbnailUrl

def getS3Image(bucket, s3ObjectKey):
    response = s3.get_object(Bucket=bucket, Key=s3ObjectKey)
    imageContent = response['Body'].read()

    file = io.BytesIO(imageContent)
    img = PIL.Image.open(file)
    return img

def getImageThumbnail(img):
    return img.resize(
        size = (thumbnailSize,thumbnailSize),
        resample = PIL.Image.LANCZOS
    )

def newFilename(s3ObjectKey):
    keySplit = s3ObjectKey.rsplit('.', 1)
    return f"{keySplit[0]}_thumbnail.{keySplit[1]}"

def uploadToS3(bucket, thumbnailFileName, image):
    outThumbnail = io.BytesIO()
    # get filetype from the file's extension
    fileType = thumbnailFileName.rsplit('.', 1)[1]
    image.save(outThumbnail, fileType)
    outThumbnail.seek(0)

    response = s3.put_object(
        ACL='public-read',
        Body=outThumbnail,
        Bucket=bucket,
        ContentType=f"image/{fileType}",
        Key=thumbnailFileName
    )
    print(response)

    url = '{}/{}/{}'.format(s3.meta.endpoint_url, bucket, thumbnailFileName)
    return url