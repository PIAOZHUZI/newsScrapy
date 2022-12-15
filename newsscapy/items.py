# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NaverscraperItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    preview = scrapy.Field()

