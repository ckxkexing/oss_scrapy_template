import os
import time
import scrapy
import json
import random
from fake_useragent import UserAgent
from scrapy.downloadermiddlewares.retry import get_retry_request

class GetGitHubReposInfoSpider(scrapy.Spider):
    name = 'get_github_repos_info_spider'
    allowed_domains = ['github.com']
    cur_page = 1
    ua = UserAgent(use_cache_server=False)
    tokens = []
    
    def __init__(self, owner_name=None, repo_name=None, info=None, *args, **kwargs):
        super(GetGitHubReposInfoSpider, self).__init__(*args, **kwargs)
        self.owner_name = owner_name
        self.repo_name = repo_name
        self.job_info = info    # ['issues', 'commits', 'pulls', 'comments']
        with open('tokens_my.json', 'r') as f:
            self.tokens = json.load(f)

    def start_requests(self):
        yield self.next_request()

    def next_request(self):
        url = 'https://api.github.com/repos'
        url = url + '/' + self.owner_name + '/' + self.repo_name + '/' + self.job_info + '?per_page=100&page=' + str(self.cur_page) + "&state=all"

        return scrapy.Request(url, callback = self.parse, headers = {
                "User-Agent" :  self.ua.random,
                'Accept': 'application/vnd.github.v3+json',
                'Accept-Language': 'en',
                'Authorization': 'token ' + random.choice(self.tokens)
            })

    def parse(self, response):
        if response.status != 200:
            # self.crawler.engine.pause()
            print("速度太快  暂停3秒")
            time.sleep(3)  # If the rate limit is renewed in a minute, put 60 seconds, and so on.
            # self.crawler.engine.unpause()
            new_request = get_retry_request(response.request, reason='empty', spider=self)
            if new_request:
                yield new_request
            return
        self.cur_page += 1
        print("!!!", self.cur_page)
        json_data = json.loads(response.text) # 获取json
        datalen = len(json_data)

        for issue in json_data:
            yield issue

        if datalen == 100:
            yield self.next_request()
