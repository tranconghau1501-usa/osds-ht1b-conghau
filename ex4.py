from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import getpass

# Mở Chrome
driver = webdriver.Chrome()

# B1: Mở trang login
url_login = "https://www.reddit.com/login/"
driver.get(url_login)
my_email = 'tranconghau1501@gmail.com'
my_password = 'Hau15012004@'


actionChains = ActionChains(driver)
time.sleep(1)
for i in range(5):
    actionChains.key_down(Keys.TAB).perform()
    
actionChains.send_keys(my_email).perform()
actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys(my_password + Keys.ENTER).perform()

time.sleep(40)


# B2: Sau khi đăng nhập → đi đến trang Explore để lấy bài đăng
url_explore = "https://www.reddit.com/r/popular/"
driver.get(url_explore)
time.sleep(8)

actions = ActionChains(driver)

posts = []
SCROLL_PAUSE = 3

# B3: Thu thập 30 bài đăng
while len(posts) < 30:

    # Lấy các thẻ chứa nội dung bài đăng
    elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='tweetText']")

    for e in elements:
        text = e.text.strip()
        if len(text) > 10 and text not in posts:
            posts.append(text)
            print("Đã thu thập:", len(posts), "bài")
            if len(posts) >= 30:
                break

    # Cuộn xuống giống người dùng thật
    actions.send_keys(Keys.END).perform()
    time.sleep(SCROLL_PAUSE)

# Đóng trình duyệt
driver.quit()

# B4: Lưu vào DataFrame
df = pd.DataFrame({"Post": posts})
df.to_csv("x_30_posts.csv", index=False, encoding="utf-8-sig")

print("Đã thu thập đủ 30 bài. Lưu tại: x_30_posts.csv")
