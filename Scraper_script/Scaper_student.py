from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")

    try:
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                "/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/a"))
        )
        print("Downloadknop gevonden.")
    except:
        print("Downloadknop niet gevonden.")

finally:
    driver.quit()