# -*- coding: utf-8 -*-
import scrapy
from spidertest.items import SearchItem
from spidertest.key import key
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from spidertest.keyText import signal

class SearchSpider(scrapy.Spider):
    def __init__(self):
        dispatcher.connect(self.spider_stopped, signals.engine_stopped)  ##建立信号和槽，在爬虫结束时调用
        dispatcher.connect(self.spider_closed, signals.spider_closed)  ##建立信号和槽，在爬虫关闭时调用
    name = 'spider'
    custom_settings = {
        'ITEM_PIPELINES': {'spidertest.searchpipeline.SearchPipeline': 300}

    }

    allowed_domains = ['www.sogou.com']
    start_urls = ['https://www.sogou.com/web?query='+str(key)+'scrapy百科']

    def parse(self, response):
        item = SearchItem()
        url = response.xpath('//*[@id="main"]/div[3]/div/div[1]/h3').extract()
        item['url'] = url
        yield item

    def spider_stopped(self):
        signal = 2
