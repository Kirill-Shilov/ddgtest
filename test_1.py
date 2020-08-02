import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path

def test_1():
    driver = webdriver.Chrome()
    driver.get("http://duckduckgo.com")
    elem = findElement(By.id("search_form_input_homepage"))
    elem.clear()
    elem.send_keys("docker")
    elem.send_keys(Keys.RETURN)
    links = driver.findElements(By.tagName("a"))
    try:
        assert "https://www.docker.com/" in links
        result = "ok"
    except Exception as e:
        result = e
    finally:
        mode = "a" if os.path.exists("result_test_1") else "w"
        with open("result_test_1", mode) as f:
            f.write(result)
        driver.close()


    

