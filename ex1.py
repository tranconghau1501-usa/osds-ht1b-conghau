from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# ----- Đường dẫn đến chromedriver -----
chrome_path = r"C:\Users\LAPTOP\OneDrive\Documents\Code dùng chung\MaNguon\chromedriver-win64\chromedriver.exe"

# ----- Khởi tạo service -----
service = Service(executable_path=chrome_path)

# ----- Tuỳ chọn Chrome -----
options = Options()
options.headless = False   # True = chạy ẩn, False = hiển thị browser

# ----- Khởi tạo WebDriver -----
driver = webdriver.Chrome(service=service, options=options)

# ----- URL -----
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"

# ----- Truy cập -----
driver.get(url)

print("\n===== BEFORE =====")
print(driver.page_source)

# ----- Chờ 3 giây -----
time.sleep(3)

print("\n===== AFTER =====")
print(driver.page_source)

# ----- Đóng trình duyệt -----
driver.quit()