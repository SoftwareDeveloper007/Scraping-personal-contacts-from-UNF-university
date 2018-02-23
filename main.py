from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def scraping(first_name="", last_name="", driver=None):

    url = "http://admin.fgcu.edu/directory/index.aspx"
    if driver is None:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='WebDriver/chromedriver.exe')
        driver.maximize_window()

    driver.get(url)

    # last_name= driver.find_element_by_css_selector("input#Text1")
    last_name_entry = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#Text1"))

    )
    first_name_entry= driver.find_element_by_css_selector("input#Text2")
    submit_btn = driver.find_element_by_css_selector("input#Button1")

    last_name_entry.send_keys(last_name)
    first_name_entry.send_keys(first_name)
    submit_btn.click()

    try:
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table#DirData > tbody > tr"))

        )
        phone_num = rows[1].find_elements_by_css_selector("td")[1].text.strip()
        email = rows[1].find_elements_by_css_selector("td")[5].text.strip()

    except:
        phone_num = ""
        email = ""

    print(phone_num)
    print(email)

    driver.quit()

    return [phone_num, email]

scraping(first_name="SHANNON", last_name="ACOSTA")
# scraping(first_name="ANTHONY", last_name="ABBATE")