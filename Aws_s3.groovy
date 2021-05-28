import org.jets3t.service.impl.rest.httpclient.RestS3Service
import org.jets3t.service.security.AWSCredentials
import org.jets3t.service.model.*
import java.io.*;

bucketName='bucketname'
accessKey='accesskey'
secretKey='secretkey'
folder='D:/'

public putS3() {}
def login = new AWSCredentials( accessKey, secretKey )
def expiry = new GregorianCalendar( 2011,0,1 ).time
def s3 = new RestS3Service( login ) 
def bucket = new S3Bucket( bucketName )
args.each{fileName->
        def key="$folder/$fileName"
        def s3obj=new S3Object(bucket,newFile('D:/sample.txt'))
        s3obj.key = key
        println "\nUploading $fileName to $bucketName/$key"
        s3obj = s3.putObject( bucket, s3obj )
        def link = s3.createSignedGetUrl( bucketName, key, login, expiry, false )
        println "$fileName : $link"
        }