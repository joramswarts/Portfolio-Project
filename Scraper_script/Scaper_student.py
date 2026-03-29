import os
import time
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath(download_dir),
    "download.prompt_for_download": False
})

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")

    # klik op download

    time.sleep(5)
    files = [f for f in os.listdir(download_dir) if f.endswith(".zip")]
    if files:
        zip_path = os.path.join(download_dir, files[0])
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(download_dir)
        print("ZIP uitgepakt.")
finally:
    driver.quit()