from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("http://example.com/")
print(driver.page_source)
driver.quit()
