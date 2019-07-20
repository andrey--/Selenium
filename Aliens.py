import time
import math
import pytest

URLS = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


@pytest.mark.parametrize('URL', URLS)
class TestLogin:
    def test_find_alien_message(self, browser, URL):
        browser.implicitly_wait(5)
        link = f"https://stepik.org/lesson/{URL}/step/1"
        browser.get(link)
        input_field = browser.find_element_by_css_selector("textarea.ember-view")
        input_field.send_keys(str(math.log(int(time.time()))))
        browser.find_element_by_css_selector("button.submit-submission").click()
        hint = browser.find_element_by_css_selector("pre.smart-hints__hint").text
        assert hint == "Correct!", f"Expected 'Correct!' but got '{hint}'"
