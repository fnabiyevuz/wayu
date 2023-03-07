import time
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import requests

username = "wayu.uz"


def download_users_posts_with_periods(username):
    try:
        posts = instaloader.Profile.from_username(instaloader.Instaloader().context, username).get_posts()
        SINCE = datetime(2022, 6, 1)
        UNTIL = datetime(2023, 3, 6)

        for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            print('**********************', post.date)
            print(post.url)
            # print(post.caption)
            r = requests.get(post.url)
            with open("instagram" + str(time.time()) + ".png", 'wb') as f:
                f.write(r.content)
            print('written')

    except Exception as e:
        print(f"-------------{e}")


download_users_posts_with_periods(username)
