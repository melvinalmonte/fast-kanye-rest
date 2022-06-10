from functools import lru_cache
import json
import tweepy
import random
from yeezy_api import config
from yeezy_api.common.logger import logger

app_config = config.get_config()


def configure_twitter():
    logger.info('Setting up tweepy credentials')
    auth = tweepy.OAuth2BearerHandler(app_config.TWITTER_ACCESS_TOKEN)
    logger.info('Creating Twitter API object')
    twitter_api = tweepy.API(auth)

    return twitter_api


@lru_cache()
def tweet_list():
    twtr = configure_twitter()
    screen_name = 'kanyewest'
    logger.info('Retrieving tweets from ye\'s timeline')
    tweets = twtr.user_timeline(screen_name=screen_name, count=200, include_rts=False, tweet_mode='extended')
    all_tweets = []
    all_tweets.extend(tweets)
    oldest_id = tweets[-1].id
    while True:
        tweets = twtr.user_timeline(screen_name=screen_name, count=200, include_rts=False, max_id=oldest_id - 1,
                                    tweet_mode='extended')
        if len(tweets) == 0:
            break
        oldest_id = tweets[-1].id
        all_tweets.extend(tweets)

    logger.info(f'Retrieved a total of {len(all_tweets)} tweets from ye\'s timeline before filtering.')
    actual_tweets = [tweet.full_text for tweet in all_tweets if 'https' not in tweet.full_text]
    logger.info(f'Retrieved a total of {len(actual_tweets)} tweets from ye\'s timeline after filtering.')

    return actual_tweets


def random_tweet():
    preloaded_tweets = open('data/preloaded_tweets.json')
    if tweet_list.cache_info().hits > 0:
        logger.info('Fetching tweet list from twitter')
        tweets = tweet_list()
    else:
        logger.info('Fetching tweet list from preloaded file')
        tweets = json.load(preloaded_tweets)
    return tweets[random.randint(0, len(tweets) - 1)]
