from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

print(browser.find_element_by_id("price").text)
WebDriverWait(browser, 5000).until(EC.text_to_be_present_in_element((By.ID, 'price'), "10000 RUR"))
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()



x=browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_id("solve").click()

