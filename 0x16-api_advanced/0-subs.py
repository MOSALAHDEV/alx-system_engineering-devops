#!/usr/bin/python3
""" Module for the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """
    if not subreddit:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Google Chrome Version 89.0.142.86'
    }
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    except Exception:
        return 0
