# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import scrapy
import os
import shutil
from urllib.parse import urlparse

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyprojectPipelinex:
    def process_item(self, item, spider):
        return item


class MyprojectPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")  # 重写ImagesPipeline类的方法    # 发送图片下载请求

    def get_media_requests(self, item, info):
        image_url = item["pic_url"]
        header = {"referer": item["referer"],
                  "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
        yield scrapy.Request(image_url, headers=header)

    def file_path(self, request, response=None, info=None, *, item=None):
        folder = item["pic_title"].strip()
        # if not os.path.exists(p):
        #     os.mkdir(p)
        return folder + "/" + os.path.basename(urlparse(request.url).path)

    # def item_completed(self, results, item, info):
    #     image_path = [x["path"] for ok, x in results if exok]
    #     new_path = '%s/%s' % (self.IMAGES_STORE, item["pic_title"])
    #     new_path = new_path.strip()
    #     if not os.path.exists(new_path):
    #         os.mkdir(new_path)
    #         pic_name = image_path[0][image_path[0].find("full\\") + 6:]  # 得到的是哈希值命名的图片名
    #         old_path = self.IMAGES_STORE + "/" + image_path[0]
    #         shutil.move(old_path, new_path + "/" + pic_name)
    #         os.rename(new_path + "/" + pic_name, new_path + "/" + item["pic_name"])
    #         item["pic_url"] = new_path + "/" + item["pic_name"]
    #         return item
