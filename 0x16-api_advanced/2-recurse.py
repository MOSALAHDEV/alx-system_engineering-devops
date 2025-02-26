#!/usr/bin/python3
"""This module contains a recursive function that
queries the Reddit API and returns titles of all hot articles
for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    "fetches the titles of hot articles on a given subreddit using recursion"
    if subreddit is None:
        return print(None)
    headers = {
        'User-Agent': 'Google Chrome Version 89.0.142.86'
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return print(None)
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data'].get('after')
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list)
