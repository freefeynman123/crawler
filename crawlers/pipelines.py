# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline

class CrawlersPipeline(object):
    def process_item(self, item, spider):
        return item

# class MyImagesPipeline(ImagesPipeline):

#     def file_path(self, request, response=None, info=None):
#         return request.meta.get('filename','')

#     def get_media_requests(self, item, info):
#     	for img,title in zip(item['image_urls'],item['title']): 
# 		    img_url = img
# 		    meta = {'filename': title}
# 		    yield scrapy.Request(url=img_url, meta=meta)

class MyImagesPipeline(ImagesPipeline):

    def image_key(self, url,item):
        image_guid = item['title']
        return 'full/%s' % (image_guid)
