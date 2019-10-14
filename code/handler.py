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
    print("event:", event, "context:", context)
    
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

    img = getS3Image(bucket,s3ObjectKey)
    print(img.size)

    imgThumbnail = getImageThumbnail(img)
    print(imgThumbnail.size)

    print("finished")

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