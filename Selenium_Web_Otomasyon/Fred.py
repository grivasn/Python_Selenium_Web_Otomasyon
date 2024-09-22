from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.kaggle.com/datasets")

try:

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedStart.MuiInputBase-inputAdornedEnd.css-1gnht4k"))
    )
    search_box.send_keys("economy")
    search_box.send_keys(Keys.ENTER)


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li.MuiListItem-root.MuiListItem-gutters.MuiListItem-divider.sc-jHofgq.fqaCGK.css-iicyhe"))
    )


    target_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.MuiListItem-root.MuiListItem-gutters.MuiListItem-divider.sc-jHofgq.fqaCGK.css-iicyhe"))
    )


    target_element.click()


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-dovzVR.eItZpV.sc-gIyTxB.heGxGx"))
    )


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-dovzVR.eItZpV.sc-gIyTxB.heGxGx"))
    )


    button.click()


    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.sc-dovzVR.fXeMKX"))
    )


    buttons = driver.find_elements(By.CSS_SELECTOR, "button.sc-dovzVR.fXeMKX")


    if len(buttons) > 1:
        buttons[1].click()
    else:
        print("İkinci buton bulunamadı!")


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.MuiInputBase-input.MuiOutlinedInput-input.css-1x5jdmq"))
    )

    email_input = driver.find_element(By.CSS_SELECTOR, "input.MuiInputBase-input.MuiOutlinedInput-input.css-1x5jdmq")
    password_input = driver.find_element(By.CSS_SELECTOR, "input.MuiInputBase-input.MuiOutlinedInput-input.MuiInputBase-inputAdornedEnd.css-1uvydh2")

    email_input.send_keys("furkan.sipahi@hotmail.com")
    password_input.send_keys("6495450fb")


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-dovzVR.cVtZmU"))
    )

    final_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-dovzVR.cVtZmU"))
    )

    final_button.click()


    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.sc-dovzVR.eItZpV.sc-bMPSCK.eKMuKQ"))
    )

    final_page_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sc-dovzVR.eItZpV.sc-bMPSCK.eKMuKQ"))
    )

    final_page_button.click()


    input("Tarayıcı açık, kapatmak için Enter'a basın...")

finally:
    driver.quit()
