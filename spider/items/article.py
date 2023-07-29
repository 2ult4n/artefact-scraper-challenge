import scrapy


class Article(scrapy.Item):
    author = scrapy.Field()
    headline = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    published_at = scrapy.Field()
