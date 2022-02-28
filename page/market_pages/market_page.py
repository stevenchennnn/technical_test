# -*- coding: UTF-8 -*-

from constants.common_constants import WebTestData
from page.base_page import BasePage
from page.market_pages.market_page_locators import MarketPageLocators


class MarketPage(BasePage):
    """
    This is the class for market pages, specific methods for pages

    """

    locators = MarketPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    # Page Actions Start
    def go_to_market_page(self):
        self.go_to_page(WebTestData.TradeMarketUrl)

    def get_market_page_title(self):
        return self.get_page_title()

    def click_tab_button(self):
        self.wait_to_click(MarketPageLocators.USDT_TAB)

    def click_trade_button(self):
        self.wait_to_click(MarketPageLocators.ZIL_TRADE_BUTTON)

    def click_cookie_accept(self):
        self.wait_to_click(MarketPageLocators.COOKIE)
