from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_cart_exist(browser):
    browser.get(link)
    cart_btn = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(cart_btn) == 1, 'Кнопка не найдена или селектор не уникален'
