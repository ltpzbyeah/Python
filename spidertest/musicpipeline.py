
# -*- coding: utf-8 -*-
import re
class MusicPipeline(object):
    def __init__(self):
        self.file = open('C:/Users\Administrator/OneDrive/Python/spidertest/music.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        musicurl_text = str(item)
        musicurl_key = 'http://(.*)(?=\"\sdownload)'
        musicurl_match = re.findall(musicurl_key, musicurl_text)
        musicstring = "".join(musicurl_match)
        musicurl_result = musicstring
        self.file.write(musicurl_text)
        self.file.close()
        return item
