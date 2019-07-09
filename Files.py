import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
# elements = browser.find_elements_by_css_selector("div.first_block>div>input")
# for element in elements:
#     element.send_keys("Мой ответ")
browser.find_element_by_css_selector("div>input[placeholder='Введите имя']").send_keys("Test")
browser.find_element_by_css_selector("div>input[placeholder='Введите фамилию']").send_keys("Test")
browser.find_element_by_css_selector("div>input[placeholder='Введите Email']").send_keys("Test")
browser.find_element_by_id("file").send_keys(os.path.abspath(os.path.dirname(__file__)))
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()
