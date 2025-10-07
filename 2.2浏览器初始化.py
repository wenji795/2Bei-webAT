from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#初始化浏览器时有两个关键参数：options 和 service
# 配置浏览器选项
options = webdriver.ChromeOptions()
# options.add_argument("--headless")   # 示例：无界面模式
# options.add_argument("--disable-gpu")  # 示例：禁用 GPU

# 配置驱动服务
service = ChromeService(
    executable_path=ChromeDriverManager().install(),
    log_output="1.log"   # 将日志输出到文件
)

# 启动浏览器
driver = webdriver.Chrome(options=options, service=service)

# 打开网页
driver.get("https://www.baidu.com")
print(driver.title)

driver.quit()
