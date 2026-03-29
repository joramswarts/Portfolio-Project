import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir
})

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")
    # Download click blijft hetzelfde als vorige versie
finally:
    driver.quit()