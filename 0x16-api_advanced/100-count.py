#!/usr/bin/python3
"""
This module contains a recursive function that
queries the Reddit API and returns titles of all hot articles
for a given subreddit.
"""
import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    """ Recursive function that queries the Reddit
    API and returns titles of all hot articles
    for a given subreddit. """
    if counts is None:
        counts = Counter()
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    if after:
        url = '{}&after={}'.format(url, after)
    headers = {
        'User-Agent': 'Google Chrome Version 89.0.142.86'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    after = data['data']['after']
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title']
        clean_title = re.sub(r'[^\w\s]', '', title.lower())
        for word in word_list:
            clean_word = word.lower()
            count = clean_title.split().count(clean_word)
            if count > 0:
                counts[word] += count
    if after:
        return count_words(subreddit, word_list, after, counts)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))
