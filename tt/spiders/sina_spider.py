#coding:utf-8
from scrapy.spider import BaseSpider
from tt.items import NewsItem
from tt.items import UrlItem
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule,CrawlSpider
import re


#class SinaSpider(BaseSpider):
class SinaSpider(CrawlSpider):
	name="sina"
	allowed_domains=["www.sina.com.cn","sina.com.cn"]
	start_urls=[
		#"www.sina.com"
		"http://sports.sina.com.cn/nba/2013-04-08/06436506847.shtml"
	]


	def parse(self,response):
		#print 'yes in pares ','0'*100
		hxs=HtmlXPathSelector(response)

		newurls=hxs.select('//a/@href').extract()

		items=[]
		usefulUrls=[]
#		print 'new urls  '+'*'*35
		rule=r'http://.*\.sina\.com\.cn.+\.shtml'
		#rule=r'http://*.sina.com.cn/*.shtml'


		rules = (Rule(SgmlLinkExtractor(allow=rule, tags='a'),callback='parse'), )



		for url in newurls:
			m=re.match(rule,url)
			if m:
				usefulUrls.append(url)
			#	print url
	        
		#items.extend([self.make_request_from_url(url).replace (callback=self.parse) for url in usefulUrls])
		for url in usefulUrls:
			req=Request(url,callback=self.parse)

			yield req

		#yield usefulUrls
		itemtem=NewsItem()
		#itemtem['title']=hxs.select('//title/text()').extract()
		#itemtem['body']=hxs.select("/div[@class='blkContainerSblk']/h1[@id='artibodyTitle']/text()").extract()
		itemtem['title']=hxs.select("//div[@class='blkContainerSblk']/h1/text()").extract()
		itemtem['body']=hxs.select("//div[@id='artibody']//p/text()").extract()
		items.append(itemtem)
		#return itemtem
		yield itemtem
		#return 
		#print 'items :'+'*'*45,itemtem
	#	yield  itemtem.load_item()
