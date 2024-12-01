import scrapy


class TokpedSpider(scrapy.Spider):
    name = "tokped"
    allowed_domains = ["www.tokopedia.com"]
    start_urls = ["https://www.tokopedia.com/nocturofficialstore/product?perpage=80"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.tokopedia.com/nocturofficialstore/product', callback=self.parse,
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
        )

    def parse(self, response):
        products = response.xpath('//div[contains(@class,"css-1sn1xa2")]')

        for product in products:

            title = product.xpath('.//div[contains(@class,"prd_link-product-name")]/text()').get()
            image_url = product.xpath('.//img[contains(@class,"css-1q90pod")]/@src').get()
            product_url = product.xpath('.//div[contains(@class,"css-19oqosi")]/a/@href').get()
            price = product.xpath('.//div[contains(@data-testid,"linkProductPrice")]/text()').get()

            yield {
                'title': title,
                'image_url': image_url,
                'product_url': product_url,
                'price': price,
                'User-Agent': response.request.headers['User-Agent']
                # 'language': language
            }
