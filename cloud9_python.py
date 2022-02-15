
import boto3

#Explicit Client Configuration
boto3.set_stream_logger(name='botocore')

#credentials masked can be easily configured on the cli to remove them from code
polly = boto3.client('polly',
        region_name='us-east-1',
        aws_access_key_id='XXXXXXXXXXXXXXXXXXX',
        aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXX'
        )

result = polly.synthesize_speech(Text='I am David This is my first polly test',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the Audio from the response
audio = result['AudioStream'].read()
with open("firstpoly.mp3","wb") as file:
    file.write(audio)