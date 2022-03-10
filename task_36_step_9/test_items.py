import time


def test_button_add_to_basket_exists(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_element_by_xpath('//button[contains(@class, "btn-add-to-basket")]')
    # time.sleep(10)
    assert button, 'No button for adding good to basket'