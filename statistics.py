# -*- coding: utf-8 -*-
import scrapy

class StatisticsSpider(scrapy.Spider):
    name = 'stats'
    page_number = 2018
    start_urls = ['https://www.fantasypros.com/nfl/reports/leaders/?year=2019&start=1&end=17']

    def parse(self, response):
        chart = response.css('table > tbody > tr')

        for row in chart:
            rank = row.css('td:nth-child(1) ::text').extract()
            name = row.css('td:nth-child(2) ::text').extract()
            pos = row.css('td:nth-child(4) ::text').extract()
            points = row.css('td:nth-child(5) ::text').extract()

            yield {
                'Rank': rank,
                'Name': name,
                'Position': pos,
                'Points': points
            }
        
        next_page = 'https://www.fantasypros.com/nfl/reports/leaders/?year='+ str(StatisticsSpider.page_number) +'&start=1&end=17'
        if StatisticsSpider.page_number > 2011:
            StatisticsSpider.page_number -= 1
            yield response.follow(next_page, callback = self.parse)  

