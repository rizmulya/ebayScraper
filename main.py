from Spiders.ebay import EbaySpider


spider = EbaySpider()
spider.exec(
    search_keywords = "book", 
    page_to_scrape = 3, #upto166
    output_csv = "Reports/ebay_data.csv",
    output_json = "Reports/ebay_data.json"
)
