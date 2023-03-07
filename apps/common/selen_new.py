import time
import urllib.request
import instaloader
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

from apps.common.models import InstaPost


def web_scraping(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.instagram.com")
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    username.send_keys("t1e9s9t9")
    password.clear()
    password.send_keys("fazliddin99")

    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()

    time.sleep(5)
    alert = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    alert2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(5)
    driver.get("https://www.instagram.com/wayu.uz/")
    time.sleep(5)
    n_scrolls = 1
    for _ in range(n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    anchors = [a.get_attribute('href') for a in anchors]
    parent_dir = "/media/fn/d/projects/UIC/wayu/media/instagram"

    for i, a in enumerate(anchors):
        if str(a).startswith("https://www.instagram.com/p/"):
            L = instaloader.Instaloader()
            post = instaloader.Post.from_shortcode(L.context, a.split("/")[-2])
            if not post.is_video:
                photo = urllib.request.urlretrieve(str(post.url), f"{parent_dir}/{i}.jpg")
                InstaPost.objects.create(url=a, photo=f"instagram/{i}.jpg", caption=post.caption)
    return HttpResponse('Done')
