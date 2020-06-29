# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ImagesItem(Item):
    collection = table = 'image'

    id = Field()
    url = Field()
    title = Field()
    thumb = Field()
