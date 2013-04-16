# Scrapy settings for tt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tt'

SPIDER_MODULES = ['tt.spiders']
NEWSPIDER_MODULE = 'tt.spiders'
ITEM_PIPELINES=['tt.pipelines.fileStore']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tt (+http://www.yourdomain.com)'
