"""Module GuardianSpider Spider craweling through the gaurdian news website extracting news data"""
import scrapy
from items.article import Article
from providers.spider_config_provider import SpiderConfigProvider
from functools import partial



class GuardianSpider(scrapy.Spider):
    """Scrapy Class for The Guardian news website Spider"""

    name = 'guardian_spider'
    start_urls = ['https://www.theguardian.com/world/all']

    def parse(self, response):
        _spider_config_provider = SpiderConfigProvider()

        for article_url in response.xpath(_spider_config_provider.xpath_article_url).extract():
            yield scrapy.Request(
                url=article_url,
                callback=partial(self.parsearticle, _spider_config_provider=_spider_config_provider)
            )
        
        next_page = response.xpath(_spider_config_provider.xpath_paginaition).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parsearticle(self, response, _spider_config_provider):
        # Test if the article is already crawled
        if 'cached' in response.flags:
            return
        item = Article()

        item['author'] = response.xpath(_spider_config_provider.xpath_author).extract()
        item['headline'] = response.xpath(_spider_config_provider.xpath_headline).extract_first()
        item['content'] = ''.join(response.xpath(_spider_config_provider.xpath_content).extract())
        item['published_at'] = response.xpath(_spider_config_provider.xpath_publish_date).extract_first()
        item['url'] = response.request.url

        yield item
