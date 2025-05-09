import sys
from Crawler import Crawler
from Reminder import Reminder

# base_currency = sys.argv[1]     # 基础货币（准备被兑换的货币）
# quote_currency = sys.argv[2]    # 报价货币（兑换的目标货币）
''' Test crawler
crawler = Crawler()
try:
    crawler.GoPage("http://fx.cmbchina.com/")
    crawler.LocateTable()
except Exception as e:
    print(f"Error: {e}")
finally:
    crawler.Close()

'''

# test Reminder
reminder = Reminder()
ret = reminder.send_email()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")