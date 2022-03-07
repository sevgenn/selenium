import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(value: str) -> str:
    return str(math.log(abs(12 * math.sin(int(value)))))


def get_alert_key(driver) -> str:
    alert = driver.switch_to.alert
    return alert.text.split()[-1]


url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome('./drivers/chromedriver')
    browser.get(url)

    button = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()

    value = browser.find_element(By.ID, 'input_value').text
    answer = calc(value)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    browser.find_element(By.ID, 'solve').click()

    print(get_alert_key(browser))
    print('>>DONE!')
except Exception as err:
    print(f'>>{err}')
finally:
    browser.quit()
