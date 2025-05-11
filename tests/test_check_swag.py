# from selenium import webdriver
from selenium.webdriver.common.by import By

# def test_icon_exist():
#     driver = webdriver.Chrome()
#     driver.get("https://www.saucedemo.com/")
#     icon = driver.find_element(By.CSS_SELECTOR, '#app > header > a')
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')

from pages.swag_labs import SwagLabs

import time

def test_check_swag(browser):
#     browser.get("https://www.saucedemo.com/")
#
#     icon = browser.find_element(By.CSS_SELECTOR, 'div.login_logo')
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')

    #
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    time.sleep(3)
    assert demo_qa_page.exist_icon()
    time.sleep(3)
    assert demo_qa_page.exist_username()
    time.sleep(3)
    assert demo_qa_page.exist_password()


    # # time.sleep(3)
    # demo_qa_page.click_on_the_icon()
    # # time.sleep(3)
    # assert demo_qa_page.equal_url()

    # assert demo_qa_page.equal_url()
