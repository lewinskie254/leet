const accountSid = 'AC2a5ba58d6260be9f814fb0e6aeb68527';
const authToken = '93bdfae4b6e3a137cdf4bae4a9698182';
const client = require('twilio')(accountSid, authToken);

client.messages
    .create({
        body: 'Hello from Twilio',
        from: '+13613360414',
        to: '+18777804236'
    })
    .then(message => console.log(message.sid))
    .done();