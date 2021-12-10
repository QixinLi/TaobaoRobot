# encoding: utf-8
# @author: liqixin.liuchuan
# @file: fuck.py
# @time: 2021/12/10 上午11:23
# coding=utf-8
from selenium import webdriver
import datetime
import time

# 此处chromedriver改为自己下载的路径
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
# driver.maximize_window()

def login():
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print("login success:", now.strftime("%Y-%m-%d %H:%M:%S"))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(buytime)
        print(now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    driver.find_element_by_link_text("提交订单").click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # 请输入抢购时间(例如格式：2018-11-11 00:00:00):
    times = "2021-12-00 12:00:00"
    login()
    buy(times)
