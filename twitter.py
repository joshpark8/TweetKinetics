<<<<<<< HEAD
# -*- coding: utf-8 -*-

import requests
import os
import json

bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
search_url = "https://api.twitter.com/2/"

# start_time,end_time,since_id,until_id,max_results,next_token,
#   expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'from:chiw00k','tweet.fields': 'author_id'}
=======
import requests
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from os import environ

base_url = "https://api.twitter.com/2/"
redirect_uri = "https://www.joshpark.dev/tweetkinetics"
oauth_url = f'{base_url}oauth2/'

bearer_token = environ.get("TWITTER_BEARER_TOKEN")
client_id = environ.get("TWITTER_OAUTH_CID")
client_secret = environ.get("TWITTER_OAUTH_CLIENT_SECRET")
scope = 'tweet.read%20users.read%20follows.read%20follows.write'
# start_time,end_time,since_id,until_id,max_results,next_token,
#   expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'from:johngreen','tweet.fields': 'author_id'}
twitter = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)
authorization_url, state = twitter.authorization_url(oauth_url)

twitter = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# # Redirect user to Spotify for authorization
# authorization_url, state = twitter.authorization_url('https://twitter.com/i/oauth2/')
# print('Please go here and authorize: ', authorization_url)

# # Get the authorization verifier code from the callback url
# redirect_response = input('\n\nPaste the full redirect URL here: ')
# auth = HTTPBasicAuth(client_id, client_secret)


>>>>>>> 48124d0 (test3)

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
<<<<<<< HEAD
    # print(response.status_code) # uncomment if 
=======
    # print(response.status_code) # uncomment if needed to debug
>>>>>>> 48124d0 (test3)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def connect_to_endpoint2(url):
    response = requests.get(url, auth=bearer_oauth)
<<<<<<< HEAD
    print(response.status_code)
=======
    # print(response.status_code) # uncomment if needed to debug
>>>>>>> 48124d0 (test3)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_recent_IDs():
<<<<<<< HEAD
    json_response = connect_to_endpoint(f'{search_url}tweets/search/recent', query_params)
=======
    json_response = connect_to_endpoint(f'{base_url}tweets/search/recent', query_params)
>>>>>>> 48124d0 (test3)
    ids = []
    for tweet in json_response['data']:
        ids.append(tweet['id'])
    return ids

def get_likes():
<<<<<<< HEAD
    like_list = []
    for id in get_recent_IDs():
        r = connect_to_endpoint2(f'{search_url}tweets?ids={id}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics')['data'][0]
        like_list.append(r['public_metrics']['like_count'])
    return like_list


if __name__ == "__main__":
    print(get_likes())
=======
    likes = []
    for id in get_recent_IDs():
        r = connect_to_endpoint2(f'{base_url}tweets?ids={id}&tweet.fields=public_metrics')['data'][0] # &expansions=attachments.media_keys&media.fields=public_metrics')['data'][0]
        likes.append(r['public_metrics']['like_count'])
    return likes
    
def get_tweets():
    tweets = []
    for id in get_recent_IDs():
        r = connect_to_endpoint2(f'{base_url}tweets?ids={id}&tweet.fields=public_metrics')['data'][0] # &expansions=attachments.media_keys&media.fields=public_metrics')['data'][0]
        tweets.append(r['text'])
    return tweets

def get_impressions():
    tweets = []
    for id in get_recent_IDs():
        r = connect_to_endpoint2(f'{base_url}tweets/{id}?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys') # &expansions=attachments.media_keys&media.fields=public_metrics')['data'][0]
        tweets.append(r)
        return tweets
    return tweets




if __name__ == "__main__":
    tweets = get_tweets()
    likes = get_likes()
    test_url = f"https://twitter.com/i/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={(redirect_uri)}&scope={scope}&state=state&code_challenge=challenge&code_challenge_method=plain"
    print(test_url)

    # impressions = get_impressions() # not public
    # print(f'{impressions}\n')
    # for like, tweet in zip(likes, tweets):
    #     print(f'{like}: {tweet}')
>>>>>>> 48124d0 (test3)
