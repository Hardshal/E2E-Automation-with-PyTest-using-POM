from selenium.webdriver.common.by import By


class DeliveryPage:

    def __init__(self, driver):
        self.driver = driver

    AddToCart = (By.CSS_SELECTOR, "a[class*=btn-primary")
    Success = (By.CSS_SELECTOR, "button[class*='btn-success']")
    AddLocation = (By.ID, "country")
    Location = (By.LINK_TEXT, 'India')
    CheckBox = (By.CSS_SELECTOR, "label[for = 'checkbox2']")
    Place = (By.CSS_SELECTOR, "input[class*='btn-success']")
    Message = (By.CLASS_NAME, "alert-success")
    def addtoCart(self):
        return self.driver.find_element(*DeliveryPage.AddToCart)

    def success(self):
        return self.driver.find_element(*DeliveryPage.Success)

    def addLoc(self):
        return self.driver.find_element(*DeliveryPage.AddLocation)

    def location(self):
        return self.driver.find_element(*DeliveryPage.Location)

    def checkBox(self):
        return  self.driver.find_element(*DeliveryPage.CheckBox)

    def placeOrder(self):
        return self.driver.find_element(*DeliveryPage.Place)

    def successMsg(self):
        return  self.driver.find_element(*DeliveryPage.Message)