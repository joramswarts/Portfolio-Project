from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")
    time.sleep(5)
finally:
    driver.quit()