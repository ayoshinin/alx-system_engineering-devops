
#!/usr/bin/python3
'''Queries the Reddit API and prints the titles of the first 10 post listed.
'''
import requests

URL = 'https://www.reddit.com'
'''Reddit's API URL.
'''

def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a subreddit.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        '{}/r/{}/.json?sort={}&limit={}'.format(
            URL,
            subreddit,
            'top',
            10
        ),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)

