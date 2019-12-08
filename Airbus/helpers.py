# import tweepy as tw
# import requests
#
# from Airbus.models import Feed
#
# TWITTER_API_KEY = 'Z5Q31pigb24XXgNBybEey0h93'
# TWITTER_API_SECRET = 'Rd1k57MA2SIwaTvDvlJQkowsjRHN2pZHBYcjeSYEUhn0VTU2CH'
# TWITTER_ACCESS_KEY = '844550287268462592-xtoIiBCriBZB6IyW20JFGyIEvcNzJ4L'
# TWITTER_ACCESS_SECRET = '0bVdpNKwvHncmHtpACksiHkIgsBkZzqv9DDfwksuK4WUv'
#
#
# def populate():
#     auth = tw.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
#     auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
#
#     api = tw.API(auth, wait_on_rate_limit=True)
#
#     tweets = tw.Cursor(api.search,
#                        q="#airbus",
#                        lang="en",
#                        since="2019-01-01").items(100)
#
#     try:
#         Feed.objects.using('news').all().delete()
#     except Exception:
#         print('Faled to delete objects')
#
#     for i in tweets:
#         try:
#             tweet = i._json
#             f = Feed(text=tweet['text'], user=tweet['user']['name'], profile_picture=tweet['user']['profile_image_url'],
#                      full_post=None)
#             f.save(using='news')
#         except Exception:
#             print('Error in saving tweet', tweet)
#
