#!/usr/bin/python3
"""
recursive function that queries Reddit API & returns list containing titles
of all hot articles for a given subreddit.
If no results are found return None.
"""

import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """Recursion that returns a list of all hot articles"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set custom headers
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    if after != "tmp":
        url = url + "?after={}".format(after)
    response = requests.get(url, headers=headers, allow_redirects=False)

    results = response.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for i in results:
        hot_list.append(i.get('data').get('title'))

    after = response.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
