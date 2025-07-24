from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create Chrome options (optional)
options = Options()
options.add_argument("--window-size=1920x1080")

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

# Navigate to a website
driver.get("https://www.google.com")

# Get page title
print(driver.title)

# Close the browser
driver.quit()