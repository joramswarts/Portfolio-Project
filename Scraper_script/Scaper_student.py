import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath(download_dir)
})

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")

    # klik op download
    # ...

    # check op ZIP-bestand
    time.sleep(5)
    files = [f for f in os.listdir(download_dir) if f.endswith(".zip")]
    if files:
        print("ZIP-bestand gevonden:", files[0])
    else:
        print("Geen ZIP-bestand gedownload.")
finally:
    driver.quit()