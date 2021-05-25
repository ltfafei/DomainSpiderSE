#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import urllib3, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class webMaster_driver():
    def __init__(self):
        # 初始化driver
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def webMaster_domain_Crawl(self, url, files):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        url = f"http://rank.chinaz.com/all/{url}"
        self.driver.get(url)
        time.sleep(1)
        page_list = self.driver.find_elements_by_xpath("//div[@id='pagelist']/a")
        #只有一页子域名爬取情况
        if len(page_list) == 0:
            print("\n \033[31m[+] 子域名只有一页，正在爬取...")
            url_list = self.driver.find_elements_by_xpath("//td[@class='bor-r1s subdomain']/a")
            for a in url_list:
                urlstr = a.text
                with open(files, "a") as fw:
                    fw.write(urlstr + "\n")
            print("\n [down] 所有子域名爬取完成")
        #多页子域名爬取情况
        else:
            print("\n \033[31m[+] 正在爬取所有页面子域名...")
            for a in page_list:
                #不直接使用a.click()，避免元素定位相互覆盖
                self.driver.execute_script("arguments[0].click()", a)
                time.sleep(2)
                url_list = self.driver.find_elements_by_xpath("//td[@class='bor-r1s subdomain']/a")
                for a in url_list:
                    urlstr = a.text
                    with open(files, "a") as fw:
                        if urlstr.split():  #去除空行
                            fw.write(urlstr+ "\n")
            print("\n [down] 所有子域名爬取完成")