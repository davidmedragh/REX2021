
import boto3

#Explicit Client Configuration
boto3.set_stream_logger(name='botocore')

#credentials masked can be easily configured on the cli to remove them from code
polly = boto3.client('polly',
        region_name='us-east-1',
        aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        )

result = polly.synthesize_speech(Text='we are honored to be invited here to give you our feedback on this AWS re:invent 2021 Thank you again for your \
                                trust on us be assured that everything we learned at Vegas will not stay in Vegas but will be well and truly at the service of euler hermes ',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the Audio from the response
audio = result['AudioStream'].read()
with open("reinvent2021.mp3","wb") as file:
    file.write(audio)