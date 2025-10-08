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
#根据css selector定位
#id选择器  #id表示用id来定位
driver.find_element(By.CSS_SELECTOR,"#userA").send_keys("admin")
#属性选择器  [属性=属性值]来定位
driver.find_element(By.CSS_SELECTOR,"[placeholder=请输入密码]").send_keys("123456")
#类名选择器  .类名表示用class来定位
driver.find_element(By.CSS_SELECTOR,".telA").send_keys("13088888888")
#类名选择器  多个类名也适用
driver.find_element(By.CSS_SELECTOR,".emailA.dzyxA").send_keys("wakawaka@qq.com")
#标签名选择器  注意默认返回符合条件的第一个标签
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"button").click()

#层级选择器
#元素A > 元素B  父元素A下的子元素B
#元素A 元素B  父元素A下的任意后代子元素B
driver.find_element(By.CSS_SELECTOR,"p > input").send_keys("111")
driver.find_element(By.CSS_SELECTOR,"p input").send_keys("222")
driver.find_element(By.CSS_SELECTOR,"p[id=pa] > input").send_keys("333")
driver.find_element(By.CSS_SELECTOR,"p[id ='pa'] > input").send_keys("444")
driver.find_element(By.CSS_SELECTOR,"div[class ='zc'] input").send_keys("555")
driver.find_element(By.CSS_SELECTOR,"div.zc input").send_keys("666")



#等待
time.sleep(5)