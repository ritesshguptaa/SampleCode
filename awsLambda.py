import os
import boto3
import urllib



def lambda_handler(event, context):
 
  transcoder = boto3.client('elastictranscoder', 'us-east-1')
  #pipeline_id = get_pipeline(transcoder, 'Audio Files')
  pipeline_id = '1542792399420-5itz1q'
  
  
  base_filename_ext = os.path.basename(event['Records'][0]['s3']['object']['key'])
  
  dir_name = os.path.dirname((event['Records'][0]['s3']['object']['key']))
  listPath = dir_name.split("/")
  
  base_filename_space = base_filename_ext.replace("+", " ")
  base_filename_nospace = base_filename_ext.replace("+", "-")
   
   #(dir_name,base_filename1) = os.path.split((event['Records'][0]['s3']['object']['key']))
   #base_filename = os.path.splitext(event['Records'][0]['s3']['object']['key'])[0]
  base_filename = os.path.splitext(base_filename_nospace)[0]
  
  if 'appvideo' in listPath :
   
   job =  transcoder.create_job(
       PipelineId=pipeline_id,
       Input={
           'Key': create_aws_filename(dir_name, base_filename_space, '') ,
           'FrameRate': 'auto',
           'Resolution': 'auto',
           'AspectRatio': 'auto',
           'Interlaced': 'auto',
           'Container' : 'auto',
       },
       Outputs=[
           {
           'Key': create_aws_filename( dir_name , 'thrash'+ base_filename, '.mp3'),
           'PresetId': '1539263753954-rco815',
           #'SegmentDuration': '1',
           'ThumbnailPattern': '' + dir_name +'/'+ base_filename + '/Thumbnail_' + base_filename + '-{resolution}' + '-{count}',
           },
           {
           'Key': create_aws_filename( dir_name +'/'+ base_filename , '480_' + base_filename, '.mp4'),
           'PresetId': '1351620000001-000020'
           #Generic 480p 
           },
           #{
           #'Key': create_aws_filename(dir_name +'/'+ base_filename, '360_' + base_filename, '.mp4'),
           #'PresetId': '1351620000001-000040'
           #Generic 360p 
           #},
           {
            'Key': create_aws_filename( dir_name +'/'+ base_filename, '240_' + base_filename, '.mp4'),
            'PresetId': '1539243908519-gd0pkr'
            #Generic 240p 
            }            
       ]
   )
  
   job_id = job['Job']['Id']
   waiter = transcoder.get_waiter('job_complete')
   waiter.wait(Id=job_id)
   
   bucket = 'uploadinput'
   key =   create_aws_filename(dir_name, base_filename_space, '')
   s34 = boto3.client('s3')
   s34.delete_object(Bucket=bucket, Key=key)
   #bucket = s3.Bucket('uploadinput')
   #s3 = boto3.resouce('s3')
   #s3.Object(bucket.name,key).delete()
   

   
   return job 
   