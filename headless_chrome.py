#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://example.com/')
print(driver.page_source)
driver.quit()
