#导包
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#创建一个浏览器对象
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))

#打开某个HTML页面
# driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8CA.html")

#核心操作
#键盘操作
# el = driver.find_element(By.XPATH, "//input")
# el.send_keys("admin")
# el.send_keys(Keys.COMMAND, "a")
# time.sleep(1)
# el.send_keys(Keys.COMMAND, "c")
# time.sleep(1)
# driver.find_element(By.XPATH,"//input[@name='emailA']").send_keys(Keys.COMMAND, "v")

#鼠标操作
# actions = ActionChains(driver)
# actions.context_click(driver.find_element(By.ID, "userA")).perform()
# time.sleep(1)
# actions.move_to_element(driver.find_element(By.TAG_NAME,"button")).perform()
# time.sleep(1)

#鼠标拖拽
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/drag.html")
actions = ActionChains(driver)
red = driver.find_element(By.ID, "div1")
blue = driver.find_element(By.ID, "div2")
actions.click_and_hold(red).move_to_element(blue).release().perform()
time.sleep(1)
actions.click_and_hold(red).move_by_offset(300,300).release().perform()
time.sleep(1)
actions.drag_and_drop(red,blue).perform()

#等待
time.sleep(3)