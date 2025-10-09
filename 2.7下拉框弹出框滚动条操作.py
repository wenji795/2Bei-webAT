#导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#创建一个浏览器对象
driver = webdriver.Chrome(service=Service("/Users/swj_795/Desktop/chromedriver-mac-arm64/chromedriver"))

#打开某个HTML页面
driver.get("file:///Users/swj_795/Desktop/%E5%8C%97%E6%A2%A6%E6%B5%8B/pagetest/%E6%B3%A8%E5%86%8CA.html")

#核心操作
#下拉框用Select类来处理是原生的HTML<select>标签
# driver.find_element(By.XPATH,"//option[.='广州']").click()
# select = Select(driver.find_element(By.XPATH, "//select[@id='selectA']"))
# select.select_by_index(1)
# select.select_by_value("sz")
# select.select_by_visible_text("广州")

#弹出框
#操作alert弹窗
# driver.find_element(By.ID, "alerta").click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()
# #操作confirm弹窗
# driver.find_element(By.ID, "confirma").click()
# confirm = driver.switch_to.alert
# print(confirm.text)
# confirm.accept()

#操作prompt
# driver.find_element(By.ID, "prompta").click()
# prompt = driver.switch_to.alert
# prompt.send_keys("hello")
# time.sleep(2)
# print(prompt.text)
# prompt.dismiss()

#操作滚动条
js1 = "window.scrollTo({top:document.body.scrollHeight, behaviour:'smooth'});"
driver.execute_script(js1)
time.sleep(1)
js2 = "window.scrollTo(0,0)"
driver.execute_script(js2)
time.sleep(1)
js3 = "window.scrollTo(0,300)"
driver.execute_script(js3)
time.sleep(1)
js4 = "window.scrollBy(0,-100)"
driver.execute_script(js4)
time.sleep(1)
js5 = "window.scrollBy(0,1000000)"
driver.execute_script(js5)
#等待
time.sleep(5)