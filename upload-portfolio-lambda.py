import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes


def lambda_handler(event, context):
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:378091754354:depoy_portfolio_topic')
    
    try:
        site_bucket = s3.Bucket('chrisdodds.info')
        build_bucket = s3.Bucket('build.chrisdodds.info')
        
        site_zip = StringIO.StringIO()
        build_bucket.download_fileobj('portfolio_build.zip', site_zip)
        
        with zipfile.ZipFile(site_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                site_bucket.upload_fileobj(obj, nm,
                                           ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                site_bucket.Object(nm).Acl().put(ACL='public-read')
        
        print "Job Done!"
        topic.publish(Subject='Portfolio Deployed', Message='Portfolio site deployed successfully!')
    except:
        topic.publish(Subject='Portfolio Deploy Failed', Message='The portfolio site deployment failed.')
        raise
    return 'Job Done'
