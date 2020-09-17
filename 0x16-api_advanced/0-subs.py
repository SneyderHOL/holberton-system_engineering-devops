#!/usr/bin/python3
"""Module for making a request to an API"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers for a
    given subreddit"""
    url = 'https://www.reddit.com/api/search_subreddits.json'
    headers = {'user-agent': 'Python3/requests_library/1'}
    redirects = False
    payload = {'query': subreddit, 'exact': True}
    request_subreddit = requests.post(url, headers=headers,
                                      allow_redirects=redirects,
                                      data=payload)
    subreddit_json = request_subreddit.json()
    if subreddit_json.get('error') is None:
        return subreddit_json['subreddits'][0]['subscriber_count']
    return 0
