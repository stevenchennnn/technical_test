# -*- coding: UTF-8 -*-

import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    This is the class for all pages, include common methods for pages

    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def go_to_page(self, url):
        self.driver.get(url)
        time.sleep(3)

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self, locator):
        WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))
        return self.driver.current_url

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    def wait_to_click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator)).click()
