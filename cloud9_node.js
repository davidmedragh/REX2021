// Load the SDK
const AWS = require('aws-sdk')
const Fs = require('fs')

// Create an Polly client
const Polly = new AWS.Polly({
    signatureVersion: 'v4',
    region: 'us-east-1'
})

let params = {
    'Text': 'we are honored to be invited here to give you our feedback on this AWS re:invent 2021 Thank you again for your \
    trust on us be assured that everything we learned at Vegas will not stay in Vegas but will be well and truly at the service of euler hermes ',
    'OutputFormat': 'mp3',
    'VoiceId': 'Kimberly'
}

Polly.synthesizeSpeech(params, (err, data) => {
    if (err) {
        console.log(err.code)
    } else if (data) {
        if (data.AudioStream instanceof Buffer) {
            Fs.writeFile("./reinvent2021_node.mp3", data.AudioStream, function(err) {
                if (err) {
                    return console.log(err)
                }
                console.log("The file was saved!")
            })
        }
    }
})