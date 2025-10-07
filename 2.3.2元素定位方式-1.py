#导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#创建一个浏览器对象
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))

#打开某个HTML页面
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8CA.html")

#核心操作
#根据id定位
driver.find_element("id", "userA").send_keys("admin")
#根据name定位
driver.find_element(By.NAME, "passwordA").send_keys("123456")
#根据class name定位
driver.find_element(By.CLASS_NAME, "telA").send_keys("130000000000")
driver.find_element(By.CLASS_NAME, "emailA").send_keys("admin@qq.com")
#根据link text定位
driver.find_element(By.LINK_TEXT, "访问 新浪 网站").click()

#等待
time.sleep(5)