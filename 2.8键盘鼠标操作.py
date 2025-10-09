#导包
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#创建一个浏览器对象
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))

#打开某个HTML页面
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8CA.html")

#核心操作
#键盘操作
el = driver.find_element(By.XPATH, "//input")
el.send_keys("admin")
el.send_keys(Keys.COMMAND, "a")
time.sleep(1)
el.send_keys(Keys.COMMAND, "c")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='emailA']").send_keys(Keys.COMMAND, "v")


#等待
time.sleep(3)