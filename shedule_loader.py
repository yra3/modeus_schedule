import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from auth_info import auth_info
from sys import platform
from selenium.webdriver.common.keys import Keys

dir_name = os.path.dirname(__file__)
if platform == "linux" or platform == "linux2":
    chrome_driver = dir_name + r"/chromedriver_linux64/chromedriver"
else:
    chrome_driver = dir_name + r"\chromedriver_win32\chromedriver.exe"


url = HOST = 'https://utmn.modeus.org/'
HEADERS = {

    'Login': auth_info['login'],
    'Password': auth_info['password'],
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0',
    'Connection': 'keep-alive',
    'Accept': '*/*',
}


def open_modeus(browser, login, password):
    """get modeus url and login in opened browser"""
    browser.get(url)
    login_inputs = browser.find_element(by='id', value='userNameInput')  # form_input
    login_inputs.click()
    login_inputs.send_keys(login)
    login_inputs = browser.find_element(by='id', value='passwordInput')
    login_inputs.click()
    login_inputs.send_keys(password)
    browser.find_element(by='id', value='submitButton').click()


service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
schedule_dir = os.path.join(dir_name, "schedule_ics_files")
preferences = {"download.default_directory": schedule_dir}
options.add_experimental_option("prefs", preferences)
browser = webdriver.Chrome(options=options, service=service)
open_modeus(browser, auth_info['login'], auth_info['password'])

# download ics file for this week
download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
download_button.click()

# move to next page button and click. move to next week
next_page_button = browser.find_element(by=By.CLASS_NAME, value='fc-next-button')
actions = ActionChains(browser)
actions.move_to_element(next_page_button).click().perform()

# download ics file for next week
download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
download_button.click()
is_loaded = False

# waiting for download
time.sleep(5)
browser.close()
