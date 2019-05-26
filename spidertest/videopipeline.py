# -*- coding: utf-8 -*-
import re


class VideoPipeline(object):
    def __init__(self):
        self.file = open('C:/Users\Administrator/OneDrive/Python/spidertest/video.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        videotext = str(item)
        result = re.split('"', videotext)
        num = len(result)
        list = []
        for i in range(1, num):
            if re.match('magnet\:\?xt=urn:btih:(.*)', result[i]) != None:
                list.append(result[i])
        self.file.write(str(list) + '\n')
        self.file.close()
        return item
