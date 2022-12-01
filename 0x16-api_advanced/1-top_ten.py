#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        top ten hot post,
        or None if subreddit requested is invalid"""
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={'limit': 10})

    if response.status_code == 200:
        titles = response.json().get('data').get('children')
        for title1 in titles:
            print(title1.get('data').get('title'))
    else:
        print(None)
