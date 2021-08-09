# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # 套图名称
    pic_title = scrapy.Field()
    # 图片地址
    pic_url = scrapy.Field()
    # 图片名称
    pic_name = scrapy.Field()
    # 保存地址
    pic_path = scrapy.Field()
    # 反爬虫用的反重定向地址
    referer = scrapy.Field()
