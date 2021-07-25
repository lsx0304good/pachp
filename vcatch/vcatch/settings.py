BOT_NAME = 'vcatch'

SPIDER_MODULES = ['vcatch.spiders']
NEWSPIDER_MODULE = 'vcatch.spiders'


USER_AGENT = 'vcatch (+http://www.yourdomain.com)'

ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {
   'vcatch.pipelines.VcatchPipeline': 300,
}
