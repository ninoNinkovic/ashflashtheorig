import tweepy
import datetime as dt
import time

def get_timeline():
    consumer_key="REMOVED"
    consumer_secret="REMOVED"
    access_token= "REMOVED"
    access_token_secret="REMOVED"
    
    # Gain access to Twitter Api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Where all the sweet stuff lies.
    api = tweepy.API(auth)
    
    return api.user_timeline()


def timestamp(date):
    return time.mktime(date.timetuple())

     
def parse_time(seconds):
        day = round(seconds / 86400)
        hour = round(seconds / 3600)
        minute = round(seconds / 60)
            
        if hour > 1 and hour <= 24:
            if hour == 1:
                return "About an hour ago:"
            elif hour == 24:
                return "About a day ago:"
            else:
                return "About %i hours ago:" % hour
                
        elif seconds > 1 and minute <= 59:
            if minute < 1:
                return "Just now:"
            elif minute == 1:
                return "About a minute ago:"
            else:
                return "About %i minutes ago:" % minute
        else:
            convert_dates = timestamp(now) - seconds
            tweet_date = dt.datetime.fromtimestamp(convert_dates).strftime("%b %d, %Y")
            return "%s:" % tweet_date

#Could refactor it so an arg can specify which timeline to get...         
def get_tweets():
    """Gets all tweets from user timeline"""
    tweet_obj = get_timeline()
    global now
    now = dt.datetime.utcnow().replace(microsecond=0)
    
    tweet_info = [(parse_time(timestamp(now) - timestamp(tweet.created_at)),
                   tweet.text,
                   tweet.id)
                   for tweet in tweet_obj if "@" not in tweet.text]
    
    return tweet_info   