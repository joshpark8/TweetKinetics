# -*- coding: utf-8 -*-

import requests
import os
import json

bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
search_url = "https://api.twitter.com/2/"

# start_time,end_time,since_id,until_id,max_results,next_token,
#   expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'from:joshparrk','tweet.fields': 'author_id'}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def connect_to_endpoint2(url):#, params):
    response = requests.get(url, auth=bearer_oauth)#, params=params)
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

def get_likers():
    '''
    for id in get_recent_IDs():
        print(id)
        json_response = connect_to_endpoint2(f'{search_url}tweets/{id}/liking_users')#, query_params)
        print(json_response)'''
    like_list = connect_to_endpoint2(f'{search_url}tweets/1590595662907084801/liking_users')['data']
    return len(like_list)


if __name__ == "__main__":
    print(get_likers())