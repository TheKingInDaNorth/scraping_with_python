import scrapy

from ItemLoaderSpiderItem.items import CompanyDetailsItem
from scrapy.loader import ItemLoader

class CompanyDetailsItemLoaderSpider(scrapy.Spider):
    name = "company_details_itemloader"
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/screener/predefined/ms_technology']