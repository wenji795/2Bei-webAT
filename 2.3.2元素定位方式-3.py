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
#根据xpath定位
#路径定位  /绝对路径
# driver.find_element(By.XPATH,"/html/body/div/fieldset/form/p[1]/input").send_keys("admin")
#         //相对路径  推荐使用相对路径
driver.find_element(By.XPATH,"//input").send_keys("admin")
#标签+属性定位  //标签名[@属性名=‘属性值’]
driver.find_element(By.XPATH,"//input[contains(@placeholder, '用户')]").send_keys("在输入用户名。。。") #可以部分匹配
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("1")
driver.find_element(By.XPATH,"//*[@type='password']").send_keys("1")
driver.find_element(By.XPATH,"//input[@id='passwordA']").send_keys("1")
#用文本定位（全部匹配）
# driver.find_element(By.XPATH,"//*[text()='新浪']").click()
#用文本定位（全部匹配）
# driver.find_element(By.XPATH,"//*[.='访问 新浪 网站']").click()
#用文本定位（部分匹配）
# driver.find_element(By.XPATH,"//button[contains(., '注')]").click() #注册按钮
#and逻辑
# driver.find_element(By.XPATH,"//input[@id='passwordA' and @type='password']").send_keys("1")
driver.find_element(By.XPATH,"//input[@id='passwordA' and contains(@placeholder, '密码')]").send_keys("1")
#与层级结合
driver.find_element(By.XPATH,"//div[@class='zc'] //input[@id='passwordA']").send_keys("1")
driver.find_element(By.XPATH,"//div[@class='zc'] //p[2] /input").send_keys("1")









#等待
time.sleep(5)