import unittest
from selenium import webdriver
import time


def method_name(url):
    link = url
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(
        "div.first_block>div.form-group>input[placeholder='Введите имя']").send_keys("Test")
    browser.find_element_by_css_selector(
        "div.first_block>div.form-group>input[placeholder='Введите фамилию']").send_keys("Test")
    browser.find_element_by_css_selector("div.first_block>div.form-group>input[placeholder='Введите Email']").send_keys(
        "Test")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    unittest.main()
