from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("http://example.com/")
print(driver.page_source)
driver.quit()
