# -*- coding: utf-8 -*-
import re


class SearchPipeline(object):
    def __init__(self):
        self.file = open('C:/Users\Administrator/OneDrive/Python/spidertest/search.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        url_text = str(item)
        url_key = '\/link\?url=(.*)(?=\"\s\'\s+\'id)'
        url_match = re.findall(url_key, url_text)
        string = "".join(url_match)
        url_result = 'www.sogou.com/link?url=' + string
        self.file.write(url_result)
        self.file.close()
        return item
