# coding=utf-
import requests
import scrapy
import json
import sys
from scrapy.spiders import CrawlSpider

from spidertest.items import SpidertestItem


class musicSpider(CrawlSpider):
    name = "musicspider"
    allowed_domains = ['music.cccyun.cc']
    start_urls = [
        "https://music.cccyun.cc/?name=可不可以&type=qq"]
    headers = {"credentials": "omit", "headers": {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7", "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "pragma": "no-cache",
        "x-requested-with": "XMLHttpRequest"},
               "referrer": "https://music.cccyun.cc/?name=%E5%8F%AF%E4%B8%8D%E5%8F%AF%E4%BB%A5&type=qq",
               "referrerPolicy": "no-referrer-when-downgrade",
               "body": "input=%E5%8F%AF%E4%B8%8D%E5%8F%AF%E4%BB%A5&filter=name&type=qq&page=1",
               "method": "POST", "mode": "cors"}

    def parse(self, response):
        item = SpidertestItem()

        # 调用ajax请求
        response = requests.get(start_urls, headers=headers)
        # ajax请求返回的是json数据，通过调用json()方法得到json数据
        json = response.json()
        data = json.get('data')


