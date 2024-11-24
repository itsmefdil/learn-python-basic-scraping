from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')


web = "https://www.audible.com/adblbestsellers"
path = "/Users/mac/Development/python/python-scraping/selenium/chromedriver"
driver = webdriver.Chrome(path, chrome_options=options)
driver.get(web)
driver.maximize_window()

# pagination
pagination = driver.find_element_by_xpath('//ul[contains(@class , "pagingElements")]')
pages = pagination.find_elements_by_xpath('.//li')
last_page = pages[-2].text

current_page = 1
title = []
author = []
length = []

while current_page <= int(last_page):
    # time.sleep(3)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))
    # container = driver.find_element_by_class_name('adbl-impression-container ')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))
    # products = container.find_elements_by_xpath('./li')

    for product in products:
        try:
            title_1 = product.find_element_by_xpath('.//h3[contains(@class, "bc-size-medium")]').text
            title.append(title_1)
            author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
            length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

            print (title_1)
        except Exception as e:
            print(e)
            continue

    current_page = current_page + 1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

df = pd.DataFrame({'title': title, 'author': author, 'length': length})
df.to_csv('audible_books.csv', index=False)
# print(df)
