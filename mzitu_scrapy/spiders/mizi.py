# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider,Rule,Request
from scrapy.linkextractors import LinkExtractor
from mzitu_scrapy.items import MzituScrapyItem

class MiziSpider(CrawlSpider):
    name = 'mizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    img_urls = []
    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        #print(response.url)
        item = MzituScrapyItem()
        item['url'] = response.url
        title = response.xpath('//h2[@class="main-title"]/text()').extract()[0]
        item['name'] = title
        max_num = response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract()[0]
        for i in range(1,int(max_num)):
            page_url = response.url+"/"+str(i)
            yield Request(page_url,callback= self.get_image_url)
        item['image_urls'] = self.img_urls
        yield item

        #print(response.url,"  ",max_num,"  ",title)
    def get_image_url(self,response):
        #print('response',response.url)
        pic_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]
        #print('pic_url',pic_url)
        self.img_urls.append(pic_url)
        for i in self.img_urls:
            print('get_image_url',i)


