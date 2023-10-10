#!/usr/bin/python3
"""
function that queries Reddit API and prints titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Get top 10 hot spots"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Set User-Agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers).json()
    top_ten = response.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for i in top_ten:
        print(i.get('data').get('title'))
