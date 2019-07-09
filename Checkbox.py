import math
from selenium import webdriver
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


# human_radio = browser.find_element_by_id("robotsRule")
#
# human_checked = human_radio.get_attribute("checked")
# print("value of human radio: ", human_checked)
# # assert human_checked is not None, "Human radio is not selected by default"
# # browser.quit()

#
x=browser.find_element_by_id("input_value").text
# print(calc(x))
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_id("robotCheckbox").click()
check=browser.find_element_by_id("robotsRule")


browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()
browser.find_element_by_css_selector("button.btn.btn-default").click()
