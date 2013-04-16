# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class NewsItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #pass
    title=Field()
    body=Field()
    keyword=Field()
    link=Field()


class UrlItem(Item):
	value=Field()
