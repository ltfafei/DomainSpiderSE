#!/usr/bin/python
# Env: python3
# Author: afei00123
# -*- coding: utf8 -*-

import argparse
from webMaster_domainCrawl import webMaster_driver
from aiStand_domainCrawl import aiStand_driver

def title():
    print("")
    print('*'.center(60, '*'))
    print("github：https://github.com/ltfafei".center(50))
    print("CSDN: afei00123.blog.csdn.net".center(50))
    print("公众号：网络运维渗透".center(40))
    print("")
    print('*'.center(60, '*'))
    print("")

if(__name__ == "__main__"):
    title()
    parser = argparse.ArgumentParser(description="SearchEngine domain spider Script")
    parser.add_argument(
        '-d', '--url', type=str, required='True',
        help='please input master domain. eg: xxx.com'
    )
    parser.add_argument(
        '-f', '--files', type=str, required='True',
        help='Please input url_file path to save. eg: c:\\urls.txt'
    )
    parser.add_argument(
        '--option', type=str, default="z", choices=["a", "z"],
        help='Please input url_file path to save. eg: c:\\urls.txt'
    )
    args = parser.parse_args()
    webmaster = webMaster_driver()
    aistand = aiStand_driver()
    if (args.option == "") | (args.option == "z"):
        webmaster.webMaster_domain_Crawl(args.url, args.files)
    if args.option == "a":
        aistand.aiStand_domain_Crawl(args.url, args.files)