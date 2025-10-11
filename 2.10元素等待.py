#导包
import os.path
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#创建一个浏览器对象
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))

#打开某个HTML页面
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8CA.html")

#核心操作
# el = driver.find_element(By.XPATH, "//input[@placeholder='延时加载的输入框']")#模拟没有等待的情况

# time.sleep(5)#强制等待
# el = driver.find_element(By.XPATH, "//input[@placeholder='延时加载的输入框']")

# driver.implicitly_wait(20)#隐式等待，找到马上就执行下一步，最多20s
# el = driver.find_element(By.XPATH, "//input[@placeholder='延时加载的输入框']")

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# wait = WebDriverWait(driver,10)
# print(wait.until(EC.title_is("注册A")))
# el = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//input[@placeholder='延时加载的输入框']")
# ))
# el.send_keys("admin1")
# print(el)






#等待
time.sleep(5)