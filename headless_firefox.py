#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Don't forget to `export MOZ_HEADLESS=1`
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary()
binary.add_command_line_options('-headless')
driver = webdriver.Firefox(firefox_binary=binary)
driver.get('http://example.com/')
print(driver.page_source)
driver.quit()
