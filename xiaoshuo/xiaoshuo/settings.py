
BOT_NAME = 'xiaoshuo'

SPIDER_MODULES = ['xiaoshuo.spiders']
NEWSPIDER_MODULE = 'xiaoshuo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'xiaoshuo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   'xiaoshuo.pipelines.XiaoshuoPipeline': 300,
}
