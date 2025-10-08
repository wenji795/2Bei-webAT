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
driver.set_window_size(300,300)
driver.set_window_position(300,300)
driver.minimize_window()
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "访问 新浪 网站").click()
time.sleep(2)
#多窗口 切换到指定窗口
handles= driver.window_handles
print("handles:", handles)
print(driver.current_window_handle, driver.title)
driver.switch_to.window(handles[1])
print("handles:", handles)
print(driver.current_window_handle, driver.title)
driver.close()
time.sleep(2)



driver.find_element(By.XPATH,"//a[.='新浪']").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
driver.back()
driver.refresh()
print(driver.title)
print(driver.current_url)








#等待
time.sleep(5)