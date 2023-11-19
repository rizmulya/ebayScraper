from Driver import By, WebDriverWait, EC, pd
from Driver.WebDriver import WebDriver
from Spiders.Locator import Locator


class EbaySpider:
    def __init__(self):
        self.driver = WebDriver().driver

    def navigate_to_website(self):
        print("Navigating to the website...")
        self.driver.get("https://ebay.com")

    def search_keywords(self, input_keywords):
        print("Website loaded...")
        keywords = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.SEARCH_BOX)
        )
        keywords.clear()
        keywords.send_keys(input_keywords)
        button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.SEARCH_BTN)
        )
        button.click()

    def scrape_data(self):
        print("Scraping data...")
        names = []
        prices = []
        product_list = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(Locator.PRODUCT_LIST)
        )
        for product in product_list[1:]:
            try:
                name = WebDriverWait(product, 5).until(
                    EC.presence_of_element_located(Locator.PRODUCT_NAME)
                ).text
                price = WebDriverWait(product, 5).until(
                    EC.presence_of_element_located(Locator.PRODUCT_PRICE)
                ).text
                print(name)
                names.append(name)
                prices.append(price)
            except:
                names.append("")
                prices.append("")
        return names, prices

    def pagination(self, page_to_scrape):
        all_names = []
        all_prices = []
        if page_to_scrape < 166:  # max 10.000 (60*166)
            for i in range(1, page_to_scrape+1):
                print(f"Scraping page {i}...")
                names, prices = self.scrape_data()
                all_names.extend(names) 
                all_prices.extend(prices)
                # next_button
                if i == 1:
                    try:
                        next_page = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located(Locator.NEXT_BTN)
                        )
                        next_page = next_page.get_attribute("href")
                        self.driver.get(next_page) 
                    except:
                        pass
                else:
                    try:
                        next_page = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_all_elements_located(Locator.NEXT_BTN)
                        )
                        next_page = next_page[1] if len(next_page) > 1 else next_page[0]
                        next_page = next_page.get_attribute("href")
                        self.driver.get(next_page) 
                    except:
                        pass  
        return {"name": all_names, "price": all_prices}

    def close_driver(self):
        self.driver.close()

    def exec(self, search_keywords, page_to_scrape, output_csv=False, output_json=False):
        self.navigate_to_website()
        self.search_keywords(search_keywords)
        data = self.pagination(page_to_scrape)
        self.close_driver()

        df = pd.DataFrame(data)
        if output_csv:
            df.to_csv(output_csv, index=False)
        if output_json:
            df.to_json(output_json, orient="records", indent=4)
        print(df)
        print("Scraping successful!")
