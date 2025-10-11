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
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")

#核心操作
#尝试定位一组元素。但因为焦点的关系，无法直接定位iframe中的用户名输入框
# els = driver.find_elements(By.XPATH, "//input[@id='userA']")
# print(len(els))
# time.sleep(3)
#
#
# # -------------------------------------------
# # 1) 通过“索引”切入 iframe
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//input[@id='userA']").send_keys("admin")
# time.sleep(1)
# #
# # 回到默认页面
# driver.switch_to.default_content()
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[@id='userA']").send_keys("adminnnnnn")

# -------------------------------------------
# 2) 通过 name 或 id 切入 iframe（这里示例 id='idframe1'）
# driver.switch_to.frame("idframe1")
# driver.find_element(By.XPATH, "//input[@id='userA']").send_keys("admin")
# time.sleep(3)
#
# # 回到默认页面
# driver.switch_to.default_content()
# driver.find_element(By.XPATH, "//input[@id='userA']").send_keys("adminnnnnn")
# time.sleep(3)

# # -------------------------------------------
# 3) 通过定位到的“iframe元素对象”切入
el = driver.find_element(By.XPATH, "//iframe[@id='idframe1']")
driver.switch_to.frame(el)
driver.find_element(By.XPATH, "//input[@id='userA']").send_keys("admin")
time.sleep(3)

# driver.quit()