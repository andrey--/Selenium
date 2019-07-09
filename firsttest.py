from selenium import webdriver
import math

url = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(url)
link=str(math.ceil(math.pow(math.pi, math.e)*10000))
link1=browser.find_element_by_link_text(link)
link1.click()

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Andrii")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Kovalenko")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Odesa")
input4 = browser.find_element_by_id("country")
input4.send_keys("Ukraine")
button = browser.find_element_by_css_selector("button.btn")
button.click()