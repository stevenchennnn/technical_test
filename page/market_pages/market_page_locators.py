# -*- coding: UTF-8 -*-

from selenium.webdriver.common.by import By


class MarketPageLocators:
    USDT_TAB = (By.XPATH, "//*[contains(@class, 'e-tabs__nav-item')][text()='USDT']")
    ZIL_TRADE_BUTTON = (By.XPATH, "//*[@class='base'][text()='ZIL']/ancestor::tr//td[last()]//*[text()='Trade']")
    INSTRUMENT = (By.XPATH, "//*[@class='cell'][text()='Instrument']")
    COOKIE = (By.XPATH, "//*[contains(@class, 'optanon-allow-all accept-cookies-button')]")
