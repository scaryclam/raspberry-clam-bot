import tweepy
import ConfigParser


class TwitterBot(object):
    def __init__(self, config_file=None):
        if config_file:
            config = ConfigParser.ConfigParser()
            config.readfp(open(config_file))
            self.CONSUMER_KEY = config.get("API", "consumer_key")
            self.CONSUMER_SECRET = config.get("API", "consumer_secret")
            self.ACCESS_TOKEN = config.get("API", "access_token")
            self.ACCESS_SECRET = config.get("API", "access_secret")
        else:
            self.CONSUMER_KEY = 'shhh, its a secret!'
            self.CONSUMER_SECRET = 'shhh, its a secret!'
            self.ACCESS_TOKEN = 'shhh, its a secret!'
            self.ACCESS_SECRET = 'shhh, its a secret!'

        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_SECRET)
        self.api = tweepy.API(auth)


    def send_tweet(self, text):
        self.api.update_status(text)

