from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


class Crawler:
    def __init__(self):
        # 设置浏览器选项
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式（可选）
        chrome_options.add_argument("--disable-gpu")
        # service = Service("chromedriver-win64/chromedriver.exe")  # chromedriver 路径
        service = Service("tmp/chromedriver.exe")  # chromedriver 路径
        # 初始化 WebDriver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    # 打开目标网页
    def GoPage(self, url):
        try:
            self.driver.get(url)  # 替换为目标网站的实际 URL
            time.sleep(3)  # 等待页面加载完成
        except Exception as e:
            print(f"Error: {e}")

    # 获取表格内容
    def LocateTable(self):
        try:
            # 定位表格的页面元素对象
            table = self.driver.find_element(By.TAG_NAME, "table")
            # 把表格的每行存储到 list
            rows = table.find_elements(By.TAG_NAME, "tr")
            len_rows = len(rows)
            len_cols = len(rows[1].find_elements(By.TAG_NAME, "td"))
            # 遍历每行
            print(len_rows, " × ", len_cols)
            for row in rows:
                # 把该行每个单元格都存到 list
                cols = row.find_elements(By.TAG_NAME, "td")
                # 遍历该行单元格
                for col in cols:
                    print(col.text, end="\t")
                print()
        except NoSuchElementException:
            print("Error: No Such Element")
        except Exception as e:
            print(f"Error: {e}")

    # 关闭浏览器
    def Close(self):
        self.driver.quit()