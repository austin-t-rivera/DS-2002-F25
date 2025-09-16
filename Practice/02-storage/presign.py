#!/Users/nem2p/.pyenv/versions/3.12.2/bin/python3.12

import boto3
from botocore.exceptions import ClientError

bucket = "ds2002-resources"
object = "zips/bundle.zip"
exp_in = 30

def presign_url(bucket, object, expiration=exp_in):
    # Generate a presigned URL for the S3 object
    s3 = boto3.client('s3')
    try:
        response = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': object},
            ExpiresIn=exp_in
            )
    except ClientError as e:
        return e

    # The response contains the presigned URL
    print(response)


if __name__ == "__main__":
    presign_url(bucket, object, expiration=exp_in)
