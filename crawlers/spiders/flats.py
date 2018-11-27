import scrapy
import re
import unidecode
import numpy as np
from ..preprocess import tidy_texts


class otodom(scrapy.Spider):

    name = "otodom"
    start_urls = ['https://www.otodom.pl/wynajem/mieszkanie/warszawa/']


    def parse(self, response):
        """
        """
        # 
        for href in response.css('header.offer-item-header a::attr(href)').extract():
            yield response.follow(href, self.parse_flat)
        # next_page = response.css('li.pager-next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)


    def parse_flat(self, response):
        yield {
            **self.parse_images(response),
            **self.parse_header(response)
        }


    @staticmethod

    def parse_images(response):

        images = response.css('img::attr(src)').extract()
        scraped_image = {
            "image_urls": [image for image in images]
            }

        return scraped_image

    @staticmethod

    def parse_header(response):
        """
        """
        offer_title = response.css('h1::text').extract_first()
        offer_location = response.css('p.address-links a::text').extract()[:4]
        #
        offer_noninformative_elements = ['Mieszkanie na wynajem', 'Zobacz na mapie']
        for element in offer_noninformative_elements:
            try:
                offer_location.remove(element)
            except ValueError:
                pass
        # 
        return {
            'title': tidy_texts.tidy_string(offer_title),
            'location': [tidy_texts.tidy_string(loc).strip() for loc in offer_location]}
