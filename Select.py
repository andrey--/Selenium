import math
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


def calc(x, y):
  return str(x+y)

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x=int(browser.find_element_by_id("num1").text)
y=int(browser.find_element_by_id("num2").text)
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(calc(x, y))

browser.find_element_by_css_selector("button.btn.btn-default").click()