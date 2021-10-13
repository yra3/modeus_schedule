import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from auth_info import auth_info
from sys import platform
# waiting js
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_modeus(browser, login, password):
    """get modeus url and login in opened browser"""
    modeus_url = 'https://utmn.modeus.org/'
    browser.get(modeus_url)
    time.sleep(1)
    login_inputs = browser.find_element(by='id', value='userNameInput')  # form_input
    login_inputs.click()
    login_inputs.send_keys(login)
    login_inputs = browser.find_element(by='id', value='passwordInput')
    login_inputs.click()
    login_inputs.send_keys(password)
    browser.find_element(by='id', value='submitButton').click()


def download_schedule():
    # declare driver file path for different systems
    dir_name = os.path.dirname(__file__)
    if platform == "linux" or platform == "linux2":
        chrome_driver = dir_name + r"/chromedriver_linux64/chromedriver"
    else:
        chrome_driver = dir_name + r"\chromedriver_win32\chromedriver.exe"

    # set browser options
    service = Service(chrome_driver)
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')  # для открытия headless-браузера
    # set download folder
    schedule_dir = os.path.join(dir_name, "schedule_ics_files")
    preferences = {"download.default_directory": schedule_dir}
    options.add_experimental_option("prefs", preferences)
    # open browser
    with webdriver.Chrome(options=options, service=service) as browser:
        browser.implicitly_wait(30)
        open_modeus(browser, auth_info['login'], auth_info['password'])
        actions = ActionChains(browser)
        # download ics file for this week

        download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
        actions.move_to_element(download_button).click().perform()
        # time.sleep(3)
        # try:
        #     element = WebDriverWait(browser, 30).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "icon-icalendar"))
        #     )
        #     download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
        #     actions.move_to_element(download_button).click().perform()
        # except:
        #     print("Fuck")

        # move to next page button and click. move to next week
        next_page_button = browser.find_element(by=By.CLASS_NAME, value='fc-next-button')
        actions.move_to_element(next_page_button).click().perform()
        # try:
        #     element = WebDriverWait(browser, 30).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "fc-next-button"))
        #     )
        #     next_page_button = browser.find_element(by=By.CLASS_NAME, value='fc-next-button')
        #     actions.move_to_element(next_page_button).click().perform()
        # except:
        #     print("Fuck")

        # download ics file for next week
        download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
        actions.move_to_element(download_button).click().perform()
        # try:
        #     element = WebDriverWait(browser, 30).until(
        #         EC.presence_of_element_located((By.CLASS_NAME, "icon-icalendar"))
        #     )
        #     download_button = browser.find_element(by=By.CLASS_NAME, value='icon-icalendar')
        #     actions.move_to_element(download_button).click().perform()
        # except:
        #     print("Fuck")

        # waiting for download
        time.sleep(10)
        browser.close()

    for i, filename in enumerate(os.listdir(schedule_dir)):
        old_name = os.path.join(schedule_dir, filename)
        new_name = os.path.join(schedule_dir, str(i))
        os.rename(old_name, new_name)
