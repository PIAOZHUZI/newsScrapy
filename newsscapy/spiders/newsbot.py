import scrapy
from scrapy import Selector, Request
from scrapy.utils import response

from newsscapy.items import NaverscraperItem


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ["https://news.naver.com/"]

    start_urls = [
        'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=103&sid2=241'
    ]

    # def __init__(self,response):
    #     n = ''.join(response.xpath('(//div[@class="paging"]/a)[last()]/text()').extract()).strip()
    #     for i in (1, n):
    #         url = 'https://news.naver.com/main/list.naver?mode=LS2D&sid2=241&sid1=103&mid=shm&date=20221214&page=' + i
    #         yield self.parse(url)

    def parse(self, response):
        # '//div(@class="class명")/a[last()]'
        print(response.xpath('(//div[@class="paging"]/a)[last()]/text()').extract())
        for select in response.css('#main_content > div.list_body.newsflash_body > ul[class^=type06] > li'):
            yield self.parse_item(select)

    def parse_item(self, response):
        items = []
        item = NaverscraperItem()
        item['title'] = ''.join(response.xpath('.//dt[2]/a/text()').extract()).strip()
        item['author'] = ''.join(response.xpath('.//dd/span[2]/text()').extract()).strip()
        item['preview'] = ''.join(response.xpath('.//dd/span[1]/text()').extract()).strip()
        items.append(item)
        # yield items
        # print(item)
