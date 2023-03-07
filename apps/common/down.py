import time
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import requests
from django.http import HttpResponse

from apps.common.models import InstaPost
import urllib.request

username = "wayu.uz"


def download_users_posts_with_periods(request, username=username):
    posts = instaloader.Profile.from_username(instaloader.Instaloader().context, username).get_posts()
    SINCE = datetime(2022, 6, 1)
    UNTIL = datetime(2023, 3, 6)
    parent_dir = "/media/fn/d/projects/UIC/wayu/media/instagram"

    try:
        for post in takewhile(lambda p: p.date > SINCE, dropwhile(lambda p: p.date > UNTIL, posts)):
            tm = time.time()
            photo = urllib.request.urlretrieve(str(post.url), f"{parent_dir}/{tm}.jpg")
            InstaPost.objects.create(url=post.url, photo=f"instagram/{tm}.jpg", caption=post.caption)
    except Exception as e:
        print(f"Error : {e}")

    return HttpResponse('Done')
