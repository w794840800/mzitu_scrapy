# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
class MzituScrapyPipeline(object):
    def process_item(self, item, spider):

        print("MzituScrapyPipeline")
        return item

class MzituImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #print("get_media_requests")
        for image_url in item['image_urls']:
            reference = item['url']
            print('get_media_requests',reference)
            yield Request(image_url,meta={'reference':reference})

    def item_completed(self, results, item, info):
        print("item_completed item_completed item_completed")
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            print("item_completed item_completed item_comple222222222")
            raise DropItem("Item contains no images")
        print("item_completed item_completed item_completed11111111")
        return item

'''
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        print('file_path',item)
        '''

