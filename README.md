# oss_scrapy_template
use scrapy V2.6.1 to crawl open source project data

## fake_useragent 网路访问异常
将 fake_useragent_0.1.11.json 文件放到系统临时文件夹下
```python
import tempfile
tempfile.gettempdir() # 临时文件地址
```
