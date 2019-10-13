import requests
def createThumbnail(event, context):
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


    print("finished")
    r = requests.get("http://www.google.com")
    print(r.status_code)