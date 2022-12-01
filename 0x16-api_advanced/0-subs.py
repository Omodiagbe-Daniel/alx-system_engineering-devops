#!/usr/bin/python3
"""module queries Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """if not a valid subreddit return 0
       else number of subscribers"""

    headers = {'User-Agent': 'xica369'}
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r1 = r.json().get("data").get("subscribers")
        return (r1)
    return 0
