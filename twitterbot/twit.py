import tweepy

class TwitterBot(object):
    def __init__(self):
        self.CONSUMER_KEY = 'shhh, its a secret!'
        self.CONSUMER_SECRET = 'shhh, its a secret!'
        self.ACCESS_TOKEN = 'shhh, its a secret!'
        self.ACCESS_SECRET = 'shhh, its a secret!'

        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(auth)


    def send_tweet(self, text):
        self.api.update_status(text)

