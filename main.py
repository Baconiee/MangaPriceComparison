from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")  # Bildirimleri engellemek için

# Amazon Price

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com.tr/ref=nav_logo")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")))
search_bar1 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")
search_bar1.send_keys("tek yumruk 23")
search_bar1.send_keys(Keys.ENTER)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "a-link-normal")))
manga1 = driver.find_element(By.CLASS_NAME, "a-link-normal")
manga1.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div[6]/div[7]/div[2]/div[2]/ul/li/span/span[1]/span/a/span[2]")))
price1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[4]/div[1]/div[6]/div[7]/div[2]/div[2]/ul/li/span/span[1]/span/a/span[2]")
print(f"One-Punch Man 23 Price is: {price1.text} in Amazon")

# D&R Price

driver.get("https://www.dr.com.tr")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[4]/div[2]/input")))
search_bar2 = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/div[4]/div[2]/input")
search_bar2.send_keys("tek yumruk 23")
search_bar2.send_keys(Keys.ENTER)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "js-search-prd-item")))
manga2 = driver.find_element(By.CLASS_NAME, "js-search-prd-item")
manga2.click()
price2 = driver.find_element(By.CLASS_NAME, "salePrice")
print(f"One-Punch Man 23 Price is: {price2.text} in D&R")

# kitapyurdu.com Price

driver.get("https://www.kitapyurdu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID, "search-input")))
search_bar3 = driver.find_element(By.ID, "search-input")
search_bar3.send_keys("tek yumruk 23")
search_bar3.send_keys(Keys.ENTER)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "pr-img-link")))
manga3 = driver.find_element(By.CLASS_NAME, "pr-img-link")
manga3.click()
price3 = driver.find_element(By.CLASS_NAME, "price__item")
print(f"One-Punch Man 23 Price is: {price3.text} in kitapyurdu.com")

driver.close()






