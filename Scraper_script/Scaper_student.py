from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://archive.ics.uci.edu/dataset/320/student+performance")

    try:
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                "/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/a"))
        )
        btn.click()
        print("Download gestart.")
    except Exception as e:
        print("Error bij klikken:", e)

finally:
    driver.quit()