# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-goudengids-css"
    start_urls = [
        # 'http://www.goudengids.be/',
        #'https://www.goudengids.be/sitemap_index_nl_be.xml'
        'https://www.goudengids.be/bedrijf/Aalst/L1180354/KPM-INVEST/',
        'https://www.goudengids.be/bedrijf/Waregem/L1231136/INTERVERVOER+DE+LEERSNIJDER/'
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'profile__title': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

