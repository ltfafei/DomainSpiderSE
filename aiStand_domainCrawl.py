#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import urllib3, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from colorama import init
init(autoreset=True)

class aiStand_driver():
    def __init__(self):
        # 初始化driver
        options = Options()
        options.add_argument("--headless")  # 无界面模拟点击
        self.driver = webdriver.Chrome(options=options)

    def get_url(self, files):
        tbody = self.driver.find_elements_by_xpath("//td[@class='site']/a")
        for a in list(tbody):
            url = a.text
            with open(files, "a+") as fw:
                fw.write(url + "\n")

    def aiStand_domain_Crawl(self, url, files):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url = f'https://rank.aizhan.com/{url}/'
        self.driver.get(url)
        time.sleep(1)
        print("\n \033[31m[+] 正在爬取当前页面子域名...")
        self.get_url(files)

        #翻页爬取到倒数第二页
        while True:
            next_pg = self.driver.find_element_by_id("ajaxNext")
            next_page_num1 = next_pg.get_attribute("data-page")
            next_pg.click()
            time.sleep(1)
            next_pg = self.driver.find_element_by_id("ajaxNext")
            next_page_num2 = next_pg.get_attribute("data-page")
            if next_page_num1 < next_page_num2:
                print("\033[31m [+] 正在翻页爬取第二页至倒数第二页子域名...")
                self.get_url(files)
            else:
                break

        #爬取最后一页
        next_pg = self.driver.find_element_by_id("ajaxEnd")
        next_pg.click()
        self.get_url(files)
        print("\033[31m [+] 正在爬取最后一页子域名...")
        print("\n [done] 所有子域名爬取完毕。")