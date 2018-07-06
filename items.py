# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class article(scrapy.Item):

	annonce_link=scrapy.Field()
	titre_annonce=scrapy.Field()
	ville=scrapy.Field()
	totm2=scrapy.Field()
	adresse=scrapy.Field()
	prix=scrapy.Field()
	code_postal=scrapy.Field()
	pays=scrapy.Field()
	agence_nom=scrapy.Field()
	agence_adresse_telephone=scrapy.Field()
	site=scrapy.Field()

    
    
   
    










#annonce_link, site, titre_annonce, adresse, m2_total, prix, ville, code_postal, pays, agence_nom, agence_adresse_telephone