from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_cart_exist(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), 'корзина не найдена'
