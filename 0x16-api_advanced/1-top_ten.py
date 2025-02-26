#!/usr/bin/python3
"""This script queries Reddit API and
prints the titles of the first top 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the
    titles of the first top 10 hot posts listed
    for a given subreddit.
    """
    if not subreddit:
        return print(None)
    headers = {
        'User-Agent': 'Google Chrome Version 89.0.142.86'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return print(None)
    data = response.json()
    posts = data['data']['children']
    for post in posts[:10]:
        print(post['data']['title'])
