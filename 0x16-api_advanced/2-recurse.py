#!/usr/bin/python3
"""
Contains recurse function that queries the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom'}

    # Limit to 100 posts per request to reduce the number of API calls
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url, headers=headers,
                params=params,
                allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
