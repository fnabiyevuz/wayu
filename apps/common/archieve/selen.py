import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.instagram.com")


def web_scraping():
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
    alert = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    alert2 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(5)

    driver.get("https://www.instagram.com/wayu.uz/")
    time.sleep(5)
    n_scrolls = 2
    for _ in range(n_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
    anchors = driver.find_elements(By.TAG_NAME, 'img')
    anchors = [a.get_attribute('src') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://instagram.ftas2-1.fna.fbcdn.net")]

    print(f'Found {len(anchors)} links to images')
    print(anchors)
    with open("links.json", "w") as f:
        f.write(str(anchors))
    driver.quit()


web_scraping()