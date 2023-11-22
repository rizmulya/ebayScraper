from Spiders.ebay import EbaySpider


spider = EbaySpider()
spider.exec(
    search_keywords = "book", 
    pages_to_scrape = 3, #number of pages to scrape (up to 166)
    output_csv = "Reports/ebay_data.csv",
    output_json = "Reports/ebay_data.json"
)
