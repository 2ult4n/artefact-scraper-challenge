# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Article(scrapy.Item):
    _id = scrapy.Field()
    author = scrapy.Field()
    headline = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    published_at = scrapy.Field()
