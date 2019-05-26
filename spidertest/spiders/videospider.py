# -*- coding: utf-8 -*-
import scrapy
from spidertest.items import VideoItem
from spidertest.key import key
import threading
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from spidertest.keyText import signal

class VideoSpider(scrapy.Spider):
    def __init__(self):
        dispatcher.connect(self.spider_stopped, signals.engine_stopped)  ##建立信号和槽，在爬虫结束时调用

    name = 'videospider'
    custom_settings = {
        'ITEM_PIPELINES': {'spidertest.videopipeline.VideoPipeline': 300},

    }

    allowed_domains = ['www.btaot.com']
    start_urls = ['http://www.btaot.com/search/'+str(key)+'-hot-desc-1']

    def parse(self, response):
        item = VideoItem()
        videourl = response.xpath('//*[@id="wall"]').extract()
        item['url'] = videourl
        yield item


    # 爬虫结束时 调用本方法
    def spider_stopped(self):
        signal=0

