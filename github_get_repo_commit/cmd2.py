'''
    https://docs.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    no use shell cmd
'''
import os
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# set params 
title = 'wkentaro_gdown'
owner_name = title.split('_')[0]
repo_name  = title.split('_')[1]
job = 'pulls'
# 内容输出路径
output_path = '/data1/chenkexing/test'
new_title = os.path.join(output_path, f"{title}_repos_{job}.jsonlines")
##

settings = get_project_settings()

settings.set('FEED_FORMAT', 'jsonlines')
settings.set('FEED_URI', new_title)

process = CrawlerProcess(settings)

# get_github_repos_info_spider 是爬虫的name
process.crawl('get_github_repos_info_spider', 
                owner_name = owner_name,
                repo_name  = repo_name,
                info = job
            )

process.start() 
