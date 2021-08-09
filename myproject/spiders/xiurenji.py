import scrapy
from myproject.items import MyprojectItem
from urllib.parse import urljoin

class XiurenjiSpider(scrapy.Spider):
    name = 'xiurenji'
    allowed_domains = ['xiurenji.cc']
    start_urls = ['https://www.xiurenji.cc/MiStar/']

    def parse(self, response):
        """
        每页的套图链接
        """
        title_link_list = response.css('div.dan > a::attr(href)').getall()
        for title_link in title_link_list:
            yield scrapy.Request(url=urljoin(response.url, title_link), callback=self.pic_parse)

        # 做翻页处理，如果有下一页，则取出下一页的地址，yield：返回给parse函数真理
        # next_page_link = response.xpath('//div[@class="pager"]//a[@title="后页"]/@href').extract_first("")
        # if next_page_link:
        #     next_page_url = next_page_link.replace("..", self.top_url)
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

    def pic_parse(self, response):
        """
        进入套图链接后，处理每一页图片链接
        """
        item = MyprojectItem()
        title = response.css('div.title::text').get().replace('\r\n','')
        item["pic_title"] = title
        # 获取referer
        referer = response.url
        item["referer"] = referer
        pic_url_list = response.css('div.img img::attr(src)').getall()
        for pic_link in pic_url_list:
            pic_name = pic_link[-10:]
            item["pic_name"] = pic_name
            # pic_url = pic_link.replace("../..", self.top_url)
            item["pic_url"] = urljoin(response.url, pic_link)
            yield item

        # 同样，套图页面里也是分页了的，所以同样要处理下一页
        next_page_link = response.xpath('//a[text()="后"]/@href').get()
        if next_page_link is not None:
            yield scrapy.Request(url=urljoin(response.url, next_page_link), callback=self.pic_parse)
