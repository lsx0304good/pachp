import scrapy.cmdline

# scrapy.cmdline.execute('scrapy crawl meijuSpider'.split())

# 不显示日志
scrapy.cmdline.execute('scrapy crawl meijuSpider --nolog'.split())

# 指定类型存储，快速存储
# supports: json, jsonlines, jl, csv, xml, marshal, pickle
# scrapy.cmdline.execute('scrapy crawl meijuSpider --nolog -o meiju2.json'.split())

#