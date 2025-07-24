from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Replace with your actual chromedriver path
driver = webdriver.Chrome()

driver.get("https://www.google.com")
print("Title of the page is:", driver.title)

driver.quit()
