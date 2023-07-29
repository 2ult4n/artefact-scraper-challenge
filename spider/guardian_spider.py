"""Module GuardianSpider Spider craweling through the gaurdian news website extracting news data"""
import scrapy
from items.article import Article


class GuardianSpider(scrapy.Spider):
    """Scrapy Class for The Guardian news website Spider"""

    name = 'guardian_spider'
    start_urls = ['https://www.theguardian.com/world/all']

    def parse(self, response):
        for article_url in response.xpath('//*[contains(@class,"fc-item__link")]//@href').extract():
            yield scrapy.Request(
                url=article_url,
                callback=self.parsearticle
            )

        next_page = response.xpath(
            '//*[contains(@class,"pagination__action--static") and contains(@rel,"next")]//@href').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parsearticle(self, response):
        # Test if the article is already crawled
        if 'cached' in response.flags:
            return

        item = Article()

        item['author'] = response.xpath(
            '//*[contains(@rel,"author")]//text()').extract()
        item['headline'] = response.xpath(
            '//*[contains(@data-gu-name,"headline")]//text()').extract_first()
        item['content'] = ''.join(response.xpath(
            '//*[contains(@id,"maincontent")]//p//text()').extract())
        item['published_at'] = response.xpath(
            '//*[contains(@property,"article:published_time")]//@content').extract_first()
        item['url'] = response.request.url

        yield item
