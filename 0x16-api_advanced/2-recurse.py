#!/usr/bin/python3
"""This module contains a recursive function that
queries the Reddit API and returns titles of all hot articles
for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """ Recursively fetches the titles of hot articles on a given subreddit """
    if subreddit is None:
        return None
    headers = {
        'User-Agent': 'Google Chrome Version 89.0.142.86'
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        after = data.get('after')
        children = data.get('data').get('children')
        for child in children:
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
