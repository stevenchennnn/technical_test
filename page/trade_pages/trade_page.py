# -*- coding: UTF-8 -*-

from constants.common_constants import WebTestData
from page.base_page import BasePage
from page.trade_pages.trade_page_locators import TradePageLocators


class TradePage(BasePage):
    """
    This is the class for trade pages, specific methods for pages

    """

    locators = TradePageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def check_page_correct(self):
        if self.get_current_url(TradePageLocators.PAGE_NAME) == WebTestData.CorrectTradePageUrl:
            return True
        else:
            return False
