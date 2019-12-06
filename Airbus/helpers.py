from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from json import loads
import json, requests
from textblob import TextBlob
import re
from twython import Twython

TWITTER_API_KEY = 'Z5Q31pigb24XXgNBybEey0h93'
TWITTER_API_SECRET = 'Rd1k57MA2SIwaTvDvlJQkowsjRHN2pZHBYcjeSYEUhn0VTU2CH'
TWITTER_ACCESS_KEY = '844550287268462592-xtoIiBCriBZB6IyW20JFGyIEvcNzJ4L'
TWITTER_ACCESS_SECRET = '0bVdpNKwvHncmHtpACksiHkIgsBkZzqv9DDfwksuK4WUv'

class StdOutListener(StreamListener):
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
        self.tweets = []

    def on_data(self, data):
        if self.counter == self.limit:
            return False
        try:
            data = loads(data)
            text = re.sub(r"http\S+", "", data['text'])
            text = text.correct(TextBlob(text))
            text = text.correct()
            res = {'polarity': text.sentiment.polarity, 'text': str(text)}
            self.tweets.append(res)
            self.counter += 1
            return True
        except Exception as e:
            print(f'error on_data {e}')
        return True

    def on_error(self, status):
        print(status)


class TwitterStreamer():
    def __init__(self):
        self.listener = None

    def stream_tweets(self, hashtag_list, limit):
        self.listener = StdOutListener(limit)
        auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
        stream = Stream(auth, self.listener)
        stream.filter(track=hashtag_list)


def get_data(hashtag_list, limit):
    streamer = TwitterStreamer()
    streamer.stream_tweets(hashtag_list, limit)
    return streamer.listener.tweets


t = Twython(app_key=TWITTER_API_KEY,
            app_secret=TWITTER_API_SECRET,
            oauth_token=TWITTER_ACCESS_KEY,
            oauth_token_secret=TWITTER_ACCESS_SECRET)
