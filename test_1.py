import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os.path

def test_1():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
      
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://duckduckgo.com')
    elem = driver.find_element(By.ID, 'search_form_input_homepage')
    elem.clear()
    elem.send_keys('docker')
    elem.send_keys(Keys.RETURN)
    data = driver.find_element_by_xpath('//*[@id="r1-0"]/div/div[1]/div/a')
    try:
        assert 'https://www.docker.com' == data.text
        result = 'ok\n'
    except Exception as e:
        result = e
    finally:
        mode = 'a' if os.path.exists('/home/result_test_1') else 'w'
        with open('result_test_1', mode) as f:
            f.write(str(result))
        driver.close()
