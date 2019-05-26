# coding=utf-
import scrapy
import json
import sys

from spidertest.items import MusicItem
from spidertest.key import key
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from spidertest.keyText import signal



class musicSpider(scrapy.Spider):
    def __init__(self):
        dispatcher.connect(self.spider_stopped, signals.engine_stopped)  ##建立信号和槽，在爬虫结束时调用

    name = "musicspider"
    custom_settings = {
        'ITEM_PIPELINES': {'spidertest.musicpipeline.MusicPipeline': 300},

    }

    allowed_domains = ['music.cccyun.cc']
    start_urls = [
        "https://music.cccyun.cc/?name="+str(key)+'&type=qq']

    def parse(self, response):
        item = MusicItem()
        pass
        # jsonresponse = json.loads(response.body_as_unicode())
        #
        # item = SpidertestItem()
        # item["url"] = jsonresponse
        # constresponse = await fetch("https://music.cccyun.cc/", {"credentials": "omit", "headers": {
        #     "accept": "application/json, text/javascript, */*; q=0.01",
        #     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7", "cache-control": "no-cache",
        #     "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "pragma": "no-cache",
        #     "x-requested-with": "XMLHttpRequest"},
        #                                                          "referrer": "https://music.cccyun.cc/?name=%E5%8F%AF%E4%B8%8D%E5%8F%AF%E4%BB%A5&type=qq",
        #                                                          "referrerPolicy": "no-referrer-when-downgrade",
        #                                                          "body": "input=%E5%8F%AF%E4%B8%8D%E5%8F%AF%E4%BB%A5&filter=name&type=qq&page=1",
        #                                                          "method": "POST", "mode": "cors"});
        # print(constresponse)

        # yield item

    def spider_stopped(self):
        signal =1
