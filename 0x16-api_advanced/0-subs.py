#!/usr/bin/python3
"""
function that queries Reddit API & returns number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Return no. of active subscibers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
