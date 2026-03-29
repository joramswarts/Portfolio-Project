import selenium
import zipfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

download_dir = os.path.join(os.getcwd(), "downloads")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")

    try:
        download_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/a"))
        )
        download_button.click()
        print("Downloadknop geklikt.")
    except Exception as e:
        print(f"Kon de downloadknop niet vinden of klikken: {e}")
        driver.quit()
        exit()

    downloaded_file = None
    for _ in range(30):
        time.sleep(1)
        files = [f for f in os.listdir(download_dir) if f.endswith(".zip")]
        crdownload_files = [f for f in os.listdir(download_dir) if f.endswith(".crdownload")]
        
        if files:
            downloaded_file = os.path.join(download_dir, files[0])
            break
        elif crdownload_files:
            print("Het bestand wordt nog gedownload...")

    if not downloaded_file:
        print("Het bestand is niet volledig gedownload.")
        driver.quit()
        exit()

    print(f"Uitpakken van {downloaded_file}...")
    with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
        zip_ref.extractall(download_dir)
    print("Uitpakken voltooid.")

finally:
    driver.quit()
