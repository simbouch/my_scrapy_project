# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BookItem(scrapy.Item):
    """ Définition des champs pour stocker les données extraites """
    title = scrapy.Field()        # Le titre du livre
    price = scrapy.Field()        # Le prix du livre
    availability = scrapy.Field() # Disponibilité du livre (En stock / Rupture)
    image_url = scrapy.Field()    # Lien de l’image du livre
