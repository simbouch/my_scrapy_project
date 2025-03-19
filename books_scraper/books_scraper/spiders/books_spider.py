import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["http://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        """ Extracts books from the page and follows pagination links """
        for book in response.css("article.product_pod"):
            book_url = response.urljoin(book.css("h3 a::attr(href)").get())
            yield scrapy.Request(book_url, callback=self.parse_book)

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_book(self, response):
        """ Extracts detailed book information """
        yield {
            "title": response.css("h1::text").get(),
            "price": response.css("p.price_color::text").get(),
            "availability": response.css("p.availability::text").get().strip(),
            "image_url": response.urljoin(response.css("div.item img::attr(src)").get()),
            "rating": self.extract_rating(response),
            "genre": response.css("ul.breadcrumb li:nth-child(3) a::text").get(),
            "description": self.extract_description(response),
        }

    def extract_rating(self, response):
        """ Convert rating class names to numerical values """
        rating_classes = response.css("p.star-rating::attr(class)").get().split()
        rating_mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        return rating_mapping.get(rating_classes[1], 0) if len(rating_classes) > 1 else 0

    def extract_description(self, response):
        """ Extract book description, handling missing descriptions """
        description = response.css("article.product_page p::text").get()
        return description.strip() if description else "No description available"
