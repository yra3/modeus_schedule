import os
import time
from sys import platform

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from auth_info import auth_info

# waiting js
DEBUG = False


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


def click_download_button(browser, sleep_time):
    actions = ActionChains(browser)
    try:
        download_button = WebDriverWait(browser, 30).until(
            conditions.presence_of_element_located((By.CLASS_NAME, "icon-icalendar"))
        )
        actions.move_to_element(download_button).click().perform()
    except TimeoutException:
        print("Кнопочка грузись быстрей!!!")
    time.sleep(sleep_time)


def download_schedule(count_weeks: int = 1):
    # declare driver file path for different systems
    dir_name = os.path.dirname(__file__)
    if platform == "linux" or platform == "linux2":
        chrome_driver = dir_name + r"/chromedriver_linux64/chromedriver"
    else:
        chrome_driver = dir_name + r"\chromedriver_win32\chromedriver.exe"

    # set browser options
    service = Service(chrome_driver)
    options = webdriver.ChromeOptions()
    if not DEBUG:
        options.add_argument('headless')  # для открытия headless-браузера
    # set download folder
    schedule_dir = os.path.join(dir_name, "schedule_ics_files")
    preferences = {"download.default_directory": schedule_dir}
    options.add_experimental_option("prefs", preferences)
    # open browser
    with webdriver.Chrome(options=options, service=service) as browser:
        browser.implicitly_wait(30)
        open_modeus(browser, auth_info['login'], auth_info['password'])

        # download ics file for this week
        while not os.listdir(schedule_dir):
            click_download_button(browser, 0.5)

        for number_week in range(count_weeks - 1):
            actions = ActionChains(browser)
            # move to next page button and click. move to next week
            try:
                next_page_button = WebDriverWait(browser, 30).until(
                    conditions.presence_of_element_located((By.CLASS_NAME, "fc-next-button"))
                )
                actions.move_to_element(next_page_button).click().perform()
            except TimeoutException:
                print("Упс, модеус не прогрузился(((")

            # download ics file for i week
            while len(os.listdir(schedule_dir)) < number_week + 2:
                click_download_button(browser, 0.5)

        browser.close()

    for i, filename in enumerate(os.listdir(schedule_dir)):
        old_name = os.path.join(schedule_dir, filename)
        new_name = os.path.join(schedule_dir, str(i))
        os.rename(old_name, new_name)
