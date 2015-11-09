__author__ = 'taohongjie'

from scrapy.item import Item,Field


class TestItem(Item):

    name = Field()
    catalog = Field()
    workLocation = Field()
    recruitNumber = Field()
    detailLink = Field()
    publishTime = Field()