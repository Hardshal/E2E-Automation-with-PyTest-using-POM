from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    CardTitle = (By.XPATH,  "//div[@class='card h-100']")
    Phone = (By.XPATH,'div/h4/a')
    Match = (By.XPATH, "div/button")
    AddToCart = (By.CSS_SELECTOR, "a[class*=btn-primary")

    def selectItems(self):
        return self.driver.find_element(*CheckOutPage.CardTitle)

    def selectPhone(self):
        return self.driver.find_element(*CheckOutPage.Phone)

    def clickPhone(self):
        return  self.driver.find_element(*CheckOutPage.Match)

