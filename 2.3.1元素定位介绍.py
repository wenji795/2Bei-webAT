import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#启动浏览器
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))
#打开百度首页
driver.get("https://www.baidu.com")
#找到百度搜索框，并输入12306
driver.find_element(By.ID, "chat-textarea").send_keys("12306")
#等待，方便查看结果
time.sleep(5)

