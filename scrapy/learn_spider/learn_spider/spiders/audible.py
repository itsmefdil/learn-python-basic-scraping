import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        products = response.xpath('//li[contains(@class, "productListItem")]')

        for product in products:
            title = product.xpath('.//h3[contains(@class, "bc-size-medium")]/a/text()').get()
            author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').get()
            length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()
            language = product.xpath('.//li[contains(@class, "languageLabel")]/span/text()').get()

            # Clean up the language text
            if language:
                language = language.replace('Language: ', '').strip()

            yield {
                'title': title,
                'author': author,
                'length': length,
                'language': language
            }
