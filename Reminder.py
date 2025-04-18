# https://cloud.tencent.com/document/product/382/37745
# https://console.cloud.tencent.com/smsv2
import sys


class Reminder:
    def __init__(self, quote_currency):
        self.quote_currency = quote_currency
        self.min = sys.float_info.min
        self.max = sys.float_info.max

    def set_max(self, max):
        self.max = max

    def set_min(self, min):
        self.min = min

    def send_messages(self, number, text):
        return