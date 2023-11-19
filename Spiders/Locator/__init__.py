from Driver import By


class Locator:
    SEARCH_BOX = (By.XPATH, "//input[@class='gh-tb ui-autocomplete-input']")
    SEARCH_BTN = (By.XPATH, "//input[@class='btn btn-prim gh-spr']")
    PRODUCT_LIST = (By.XPATH, "//li[@class='s-item s-item__pl-on-bottom']")
    PRODUCT_NAME = (By.XPATH, ".//span[@role='heading']")
    PRODUCT_PRICE = (By.XPATH, ".//span[@class='s-item__price']")
    NEXT_BTN = (By.XPATH, "//nav[@role='navigation']/a")
    