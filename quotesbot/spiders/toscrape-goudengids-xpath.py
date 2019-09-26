# -*- coding: utf-8 -*-
import scrapy

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-goudengids-xpath'
    start_urls = [
        'https://www.goudengids.be/sitemap_index_nl_be.xml'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="profile__inner"]'):
            yield {
                'name': quote.xpath('./span[@class="profile__title"]/text()').extract_first(),
                'address': quote.xpath('.//small[@class="card__info fl"]/text()').extract_first(),
                'categorie': quote.xpath('.//div[@class="categories detail mb20"]/text()').extract()
            }

        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

