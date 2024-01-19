import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass

from Page_objects.HomePage import HomePage
from Page_objects.CheckOutPage import CheckOutPage
from Page_objects.DeliveryPage import DeliveryPage

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):

        Home = HomePage(self.driver)
        HomePage.shopItem(self).click()

        Item = CheckOutPage(self.driver)
        phones = [CheckOutPage.selectItems(self)]

        for phone in phones:
            name = phone.text
            if name == 'Samsung Note 8':
                print(name)
                phone.CheckOutPage.Match(self).click()

        DeliveryPage.addtoCart(self).click()

        DeliveryPage.success(self).click()

        DeliveryPage.addLoc(self).send_keys("In")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))

        DeliveryPage.location(self).click()

        DeliveryPage.checkBox(self).click()
        DeliveryPage.placeOrder(self).click()

        success = DeliveryPage.successMsg(self).text

        assert "Success" in success
