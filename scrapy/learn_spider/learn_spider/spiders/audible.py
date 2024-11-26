import scrapy



class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/adblbestsellers"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.audible.com/adblbestsellers', callback=self.parse,
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
        )



    def parse(self, response):
        products = response.xpath('//li[contains(@class, "productListItem")]')

        for product in products:
            title = product.xpath('.//h3[contains(@class, "bc-size-medium")]/a/text()').get()
            author = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').get()
            length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()
            # language = product.xpath('.//li[contains(@class, "languageLabel")]/span/text()').get()

            # Clean up the language text
            # if language:
            #     language = language.replace('Language: ', '').strip()

            yield {
                'title': title,
                'author': author,
                'length': length,
                'User-Agent': response.request.headers['User-Agent']
                # 'language': language
            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements")]')
        next_page_url = pagination.xpath('.//span[contains(@class,"nextButton")]/a/@href').get()
        pages = pagination.xpath('.//li[contains(@class, "bc-list-item")]/a/text()').getall()
        last_page = int(pages[-1])
        url= "https://www.audible.com/adblbestsellers?"
        print("Pagination: ", next_page_url)

        if pages:
                    last_page = int(pages[-1])
                    current_page = response.url.split('page=')[-1] if 'page=' in response.url else 1
                    current_page = int(current_page)

                    if current_page < last_page:
                        next_page = current_page + 1
                        next_page_url = f"{url}?page={next_page}"
                        yield response.follow(
                            url=next_page_url,
                            callback=self.parse,
                            headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
                        )

        # if next_page_url:
            # yield response.follow(url=next_page_url, callback=self.parse,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
            # )

            # yield response.follow(url=next_page_url, callback=self.parse)
