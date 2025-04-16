import sys
from Crawler import Crawler

# base_currency = sys.argv[1]     # 基础货币（准备被兑换的货币）
# quote_currency = sys.argv[2]    # 报价货币（兑换的目标货币）

crawler = Crawler()
try:
    crawler.GoPage("http://fx.cmbchina.com/")
    crawler.LocateTable()
except Exception as e:
    print(f"Error: {e}")
finally:
    crawler.Close()


