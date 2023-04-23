import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("item",
                         [
                             "Tv",
                             "samsung",
                             "apple watch"
                         ])
@pytest.mark.smoketest
def test_amazon_search(browser, item):
    browser.get("https://www.amazon.com/")
    browser.find_element(By.ID, "twotabsearchtextbox").send_keys(item)
    browser.find_element(By.ID,"nav-search-submit-text").click()
    assert item in browser.title