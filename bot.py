from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/bot', methods=['POST'])
def bot():

    #retrieving the access toekn for reddit api
    CLIENT_ID = #provide client id
    SECRET = #provide secret
    base_url = 'https://www.reddit.com/'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)
    data = {
    'grant_type': 'password',
    'username': #username,
    'password': #password
    }
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    res = requests.post(base_url + 'api/v1/access_token', auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    #setting up chatbot
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    def test():
        r = req.json()
        for post in r['data']['children'][:5]:
            msg.body("-" + post['data']['title'])
            msg.body("\n")
            responded = True
    if 'hi' in incoming_msg or 'hey' in incoming_msg or 'hello' in incoming_msg:
        msg.body("Hi there!")
        responded = True
    if 'who' in incoming_msg and 'you' in incoming_msg:
        msg.body("I am a bot created by Ansh :)")
        responded = True
    if 'how are you' in incoming_msg: 
        msg.body("I'm fine! Wish the same for you.")
        responded = True
    if 'hot' in incoming_msg and 'python' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers)
        test()
    if 'top' in incoming_msg and 'python' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/python/top', headers=headers)
        test()
    if 'new' in incoming_msg and 'python' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/python/new', headers=headers)
        test()
    if 'hot' in incoming_msg and 'java' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/java/hot', headers=headers)
        test()
    if 'top' in incoming_msg and 'java' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/java/top', headers=headers)
        test()
    if 'new' in incoming_msg and 'java' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/java/new', headers=headers)
        test()
    if 'hot' in incoming_msg and 'data science' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/datascience/hot', headers=headers)
        test()
    if 'top' in incoming_msg and 'data science' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/datascience/top', headers=headers)
        test()
    if 'new' in incoming_msg  and 'data science' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/datascience/new', headers=headers)
        test()
    if 'latest' in incoming_msg and 'news' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/news/new', headers=headers)
        test()
    if 'hot' in incoming_msg and 'machine learning' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/machinelearning/hot', headers=headers)
        test()
    if 'top' in incoming_msg and 'machine learning' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/machinelearning/top', headers=headers)
        test()
    if 'new' in incoming_msg and 'machine learning' in incoming_msg:
        req = requests.get('https://oauth.reddit.com/r/machinelearning/new', headers=headers)
        test()
    if not responded:
        msg.body("I am unable to figure out what you're trying to say.")
        responded = True

    return str(resp)

if __name__=="__main__":
    app.run()