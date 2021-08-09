# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
ROBOTSTXT_OBEY = False

IMAGES_URLS_FIELD = "pic_url"

#自定义保存路径
IMAGES_STORE = "xiannv"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟，可以自己设置，太快可能被网站ban掉
DOWNLOAD_DELAY = 0.4
# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'fa24spider.pipelines.Fa24SpiderPipeline': 300,
    'myproject.pipelines.MyprojectPipeline': 1,
}
MEDIA_ALLOW_REDIRECTS =True
