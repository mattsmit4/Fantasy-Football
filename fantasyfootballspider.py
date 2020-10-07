# -*- coding: utf-8 -*-
import scrapy

class FantasyfootballSpider(scrapy.Spider):
    name = 'fantasyfootballspider'
    #allowed_domains = ['https://fantasyfootballcalculator.com']
    page_number = 2018
    start_urls = ['https://fantasyfootballcalculator.com/adp/standard/12-team/all/2019']

    def parse(self, response):
        chart = response.css('table.table.adp > tr')
        
        for row in chart:
            pick = row.css('td:nth-child(1) ::text').extract()
            name = row.css('.adp-player-name a ::text').extract()
            pos = row.css('.adp-player-name+ td ::text').extract()  
        
            yield {
                'Pick': pick,
                'Name': name,
                'Position': pos,
            }
        
        next_page = 'https://fantasyfootballcalculator.com/adp/standard/12-team/all/'+ str(FantasyfootballSpider.page_number) +''
        if FantasyfootballSpider.page_number > 2011:
            FantasyfootballSpider.page_number -= 1
            yield response.follow(next_page, callback = self.parse)  
        
            