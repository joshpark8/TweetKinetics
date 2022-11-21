# -*- coding: utf-8 -*-

import requests
import os
import json

bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
search_url = "https://api.twitter.com/2/"

# start_time,end_time,since_id,until_id,max_results,next_token,
#   expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'from:chiw00k','tweet.fields': 'author_id'}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    # print(response.status_code) # uncomment if 
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def connect_to_endpoint2(url):
    response = requests.get(url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_recent_IDs():
    json_response = connect_to_endpoint(f'{search_url}tweets/search/recent', query_params)
    ids = []
    for tweet in json_response['data']:
        ids.append(tweet['id'])
    return ids

def get_likes():
    like_list = []
    for id in get_recent_IDs():
        r = connect_to_endpoint2(f'{search_url}tweets?ids={id}&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics')['data'][0]
        like_list.append(r['public_metrics']['like_count'])
    return like_list


if __name__ == "__main__":
    print(get_likes())