from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Đường dẫn đến chromedriver
chrome_path = r"C:\Users\LAPTOP\OneDrive\Documents\Code dùng chung\MaNguon\chromedriver.exe"
ser = Service(chrome_path)

# Tùy chọn Chrome
options = webdriver.ChromeOptions()
options.headless = False

# Khởi tạo driver
driver = webdriver.Chrome(options=options, service=ser)

# URL trang đăng nhập (ví dụ minh họa, bạn thay bằng trang thật)
url = "https://www.facebook.com/"
driver.get(url)
time.sleep(2)

# Tìm ô nhập username/email
username_input = driver.find_element(By.XPATH, "//input[@name='username']")
password_input = driver.find_element(By.XPATH, "//input[@name='password']")

# Nhập thông tin đăng nhập
username_input.send_keys("my_username")
time.sleep(1)
password_input.send_keys("my_password")

time.sleep(2)

# Tìm và click nút đăng nhập
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Chờ vài giây để trang xử lý
time.sleep(5)

# Đóng trình duyệt
driver.quit()