
BOT_NAME = 'baike'

SPIDER_MODULES = ['baike.spiders']
NEWSPIDER_MODULE = 'baike.spiders'

USER_AGENT = 'baike (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
   'baike.pipelines.BaikePipeline': 300,

   # 使用redis管道：自动存入redis,默认存入本机的redis
   # 存入到redis中的 mybaike:items 列表中
   'scrapy_redis.pipelines.RedisPipeline': 400,
}

# scrapy-redis相关的settings
# dupefilter: 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否允许暂停
SCHEDULER_PERSIST = True

# 配置远程连接redis， 默认会连接本地的Redis数据库
# REDIS_HOST = '10.23.4.5'
# REDIS_PORT = 6379
