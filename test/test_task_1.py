# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from constants.common_constants import Config, WebTestData
from logger.logger import logger
from page.market_pages.market_page import MarketPage
from page.trade_pages.trade_page import TradePage

"""
Task 1 Start

1. Go to market page
2. Pass the cookie by click button
3. Click USDT tab
4. Click ZIL/USDT trade button
5. Check page url to check correct page or not

"""


class TestTask1:

    def setup_class(self):
        options = webdriver.ChromeOptions()
        service = Service(Config.ChromeDriverPath)
        self.driver = webdriver.Chrome(service=service, options=options)
        logger.info("set driver")
        self.driver.maximize_window()

    def test_go_to_market_page(self):
        self.market = MarketPage(self.driver)
        self.market.go_to_market_page()
        title = self.market.get_market_page_title()
        logger.info("Title of this Page = %s", title)
        assert title == WebTestData.TradeMarketTitle
        logger.info("Pass Test")

    def test_pass_cookie(self):
        self.market = MarketPage(self.driver)
        self.market.click_cookie_accept()
        logger.info("Pass Test")

    def test_click_usdt_tab(self):
        self.market = MarketPage(self.driver)
        self.market.click_tab_button()
        logger.info("Pass Test")

    def test_check_and_click_trade_button(self):
        self.market = MarketPage(self.driver)
        self.market.scroll_to_bottom()
        self.market.click_trade_button()
        logger.info("Pass Test")

    def test_check_correct_page_or_not(self):
        self.trade = TradePage(self.driver)
        assert self.trade.check_page_correct()
        logger.info("Pass Test")

    def teardown_class(self):
        logger.info("driver close")
        self.driver.close()
