# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    url = scrapy.Field()#


class MusicItem(scrapy.Item):
    url = scrapy.Field()


class VideoItem(scrapy.Item):
    url = scrapy.Field()
