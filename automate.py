import schedule
import time
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

URL = "https://www.nba2kmobile.com/dailystreak"

load_dotenv()
pid = os.getenv('PLAYER_ID')


def claim_daily() -> None:
    print("running")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") #less resources to run the webpage without the GUI
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) #this installs a chromedriver to be used as a service for the webdriver
    try:
        driver.get(URL)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".onetrust-close-btn-handler"))).click() #close cookie popup
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'CLAIM') and @data-testid='list-view-buy-button']"))).click() #clicks on claim button
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Type in my Player ID') and @aria-label='Verify']"))).click() #clicks on type in player id button
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='user-id-validity']"))).send_keys(pid) #inputs my player ID into input field
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='product-redeem-button']"))).click() #clicks on submit button
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue') and @data-testid='userid-continue-button']"))).click() #clicks on continue button to verify player id
    except Exception as err:
        print(f"Cannot obtain URL for some reason {err}.")
    finally:
        driver.quit()


if __name__ == '__main__':
    schedule.every().day.at("14:02").do(claim_daily) #syntatic sugar for run_pending to know when to run claim_daily, doesn't actually schedule anything by itself
    while True:
        schedule.run_pending() #checks for time 
        time.sleep(1)
    