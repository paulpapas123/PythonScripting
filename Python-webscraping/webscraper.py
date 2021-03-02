from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#download chrome driver and get the directory for it and put it into the path variable
Path =  ''
driver = webdriver.Chrome(Path)
driver.get("https://techwithtim.net")
print(driver.title)
#finds the search bar on the page
search = driver.find_element_by_name("s")
#types in the word test to the search bar by the send_keys command and hits enter
search.send_keys("test")
search.send_keys(Keys.RETURN)

#code that waits for a page navigation
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
except:
    driver.quit()



driver.quit()
#hierarchy of accessing html elements 1:id 2:name 3:class