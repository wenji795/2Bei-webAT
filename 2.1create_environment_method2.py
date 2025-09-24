import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService

# ================= Chrome 示例 =================
# 首次运行会自动下载匹配的 chromedriver（可能比较慢）
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# ================= Edge 示例 =================
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# 打开百度首页
driver.get("https://www.baidu.com")

# 等待 5 秒，方便查看结果
time.sleep(5)

driver.quit()
