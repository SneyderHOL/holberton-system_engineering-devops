#!/usr/bin/python3
"""Module for making a request to an API"""
import json
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the first 10 hot
    listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'Python3/requests_library/1'}
    redirects = False
    request_subreddit = requests.get(url, headers=headers,
                                     allow_redirects=redirects)
    subreddit_json = request_subreddit.json()
    for title in subreddit_json['data']['children']:
        print(title['data']['title'])
