from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 设置浏览器选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式（可选）
chrome_options.add_argument("--disable-gpu")

# 初始化 WebDriver
service = Service("chromedriver-win64/chromedriver.exe")  # chromedriver 路径
driver = webdriver.Chrome(service=service, options=chrome_options)


# 获取表格内容
def LocateTable(driver):
    try:
        # 定位表格的页面元素对象
        table = driver.find_element(By.TAG_NAME, "table")
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


# 爬取汇率
try:
    # 打开目标网页
    driver.get("http://fx.cmbchina.com/")  # 替换为目标网站的实际 URL
    time.sleep(3)  # 等待页面加载完成

    # 定位美元对人民币的现汇汇率
    LocateTable(driver)

except Exception as e:
    print(f"Error: {e}")

finally:
    # 关闭浏览器
    driver.quit()

