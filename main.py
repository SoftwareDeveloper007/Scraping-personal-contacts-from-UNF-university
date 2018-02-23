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

    url = "https://banner.unf.edu/pls/nfpo/wkindir.p_search_bylastname"
    if driver is None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='WebDriver/chromedriver.exe')
        driver.maximize_window()

    driver.get(url)

    # last_name= driver.find_element_by_css_selector("input#Text1")
    last_name_entry = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#tbLNameSearch"))

    )
    submit_btn = driver.find_element_by_css_selector("input#btnLNameSearch")

    last_name_entry.send_keys(last_name)
    submit_btn.click()

    phone_num = ""
    try:
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table#gvSortByLName > tbody > tr"))

        )

        for i, row in enumerate(rows):
            if i==0:
                continue

            cols = row.find_elements_by_css_selector("td")
            name_tmp = cols[0].text.strip()
            phone_num_tmp = cols[1].text.strip()

            if first_name in name_tmp.upper() and last_name in name_tmp.upper():
                phone_num = phone_num_tmp
                break

    except:
        phone_num = ""

    print(phone_num)

    driver.quit()

    return phone_num

scraping(first_name="ANN", last_name="ADAMS")
# scraping(first_name="ANTHONY", last_name="ABBATE")