from schedule import every, run_pending
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager import ChromeDriverManager
from dotenv import load_dotenv
import os

# import requests
# from bs4 import BeautifulSoup


URL = "https://www.nba2kmobile.com/dailystreak"

load_dotenv()
pid = os.getenv('PLAYER_ID')

def write2file(content):
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(content)

def claim_daily():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #this installs a chromedriver to be used as a service for the webdriver
    try:
        driver.get(URL)
    except Exception as err:
        print(f"Cannot obtain URL for some reason {err}")
    finally:
        driver.quit()
    # print("env", pid)
    # response = requests.get(URL)
    # print(response.status_code)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # # write2file(soup.prettify())
    # button = soup.find(lambda tag: tag.name == 'button' and tag.text == 'CLAIM')
    # if button:

if __name__ == '__main__':
    claim_daily()