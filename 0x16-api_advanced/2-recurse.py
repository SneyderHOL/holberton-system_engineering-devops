#!/usr/bin/python3
"""Module for making a request to an API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that queries the Reddit API and return a list
    containing the titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'Python3/requests_library/1'}
    redirects = False
    if len(hot_list) == 0:
        request_subreddit = requests.get(url, headers=headers,
                                         allow_redirects=redirects)
    else:
        data = {'after': after}
        request_subreddit = requests.get(url, headers=headers, params=data,
                                         allow_redirects=redirects)
    if request_subreddit.status_code == 200:
        subreddit_json = request_subreddit.json()
        for children in subreddit_json['data']['children']:
            hot_list.append(children)
        end_value = subreddit_json['data']['after']
        if end_value is None:
            return hot_list
        return recurse(subreddit, hot_list, end_value)
    return None
