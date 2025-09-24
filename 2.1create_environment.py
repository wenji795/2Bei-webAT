import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#启动chrome
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))#service用于加载驱动

driver.get("https://www.google.com")
print(driver.title)

time.sleep(5)

# driver.quit()
