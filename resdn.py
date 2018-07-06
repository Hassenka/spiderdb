from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import scrapy
import re
import requests
import json 
from items import article
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class DatabizSpider(scrapy.Spider):
    MN=0
    MX=10000000000000
    name = 'databiz38'
    start_urls = ['http://www.residences-immobilier.com/fr/recherche.html?lang=FR&setLocDep=&departement=&district=&villes=&TypeAnnonceV=VEN&ville_dep=&enlarge_search=&TypeBien=&bdgMin='+str(MN)+'&bdgMax='+str(MX)+'&nb_piece=&surfMin=&surfMax=&keywords=']
    
    def parse (self,response):
        t=response.xpath('//*[@class="more_details show-for-medium js-annonce-link"]/@href').extract()
        for im in t:
            yield response.follow(im, callback=self.parse_ef)
        te=response.xpath('//*[@class="hthin"]/@href').extract()
        for ime in te:
            yield response.follow(ime, callback=self.parse_e)
       
        url_next=response.css('html body div.off-canvas-wrapper div.off-canvas-content div.row div.total_pagination.hlight.rr_nomargin.columns.small-12.no-padding div.ligne_annonces.columns.small-12.no-padding ul.pagination.text-right li a::attr(href)').extract()
        for er in url_next:
            yield response.follow(er,callback=self.parse)
    def parse_e(self,response):
        item=article()
        item['adresse']=response.xpath('//*[@itemprop="streetAddress"]/text()').extract()
        item['code_postal']=response.xpath('//*[@itemprop="postalCode"]').re(r'\d+')
        item['pays']=response.xpath('//*[@itemprop="addressLocality"]/text()').extract()
        item['agence_nom']=response.xpath('//*[@class="hthin"]/text()').extract()
        item['site']="residence_immobilier"
        yield item 
    def parse_ef(self,response):
        item=article()
        item['prix']=response.xpath('//*[@itemprop="price"]/text()').extract()
        item['ville']=response.xpath('//*[@class="ville"]/text()').extract()
        item['totm2']=response.xpath('//*[@itemprop="floorSize"]/text()').extract()
        item['annonce_link']=response.xpath('//*[@rel="canonical"]/@href').extract()
        item['titre_annonce']=response.xpath('//*[@class="ta_tb"]/text()').extract()
        yield item
        a=response.xpath('//*[@rel="canonical"]/@href').extract()
        for item in a:
            b=item
            r = requests.get(''+b)
            q=re.search(r'\Wfr/ajax/agence-tel-\d*-\d*.html',r.text)
            url_tel='http://www.residences-immobilier.com'+(q.group(0))
            yield response.follow(url_tel,callback=self.parse_tel)





    def parse_tel(self,response):
        
        item=article()
        data=json.loads(response.text)
        item['agence_adresse_telephone']=data
        yield item
       
           
          