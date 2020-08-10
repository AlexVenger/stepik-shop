link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_a_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary')
    assert button is not None, "The button doesn't exist!"
