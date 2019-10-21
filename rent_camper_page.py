from selene.api import s, by, be, ss, browser
from data import base_url


class RentCamperPage(object):
    def __init__(self):
        self.spinner = s('.spinner')

    def open_base_url(self):
        browser.driver().delete_all_cookies()
        browser.open_url(base_url + 'rent-camper/')

    def set_body_style_filter(self, search_filter):
        s(by.text('Body style')).click()
        s(by.text(search_filter)).click()
        s('.options___2FJcf.bigSize___1sgsF > .actions___1u4g_ > div > .buttonApply___2Pjua').\
            should(be.enabled).click()

    def check_body_style_is(self, search_filter):
        self.spinner.should_not(be.visible)
        body_classes = ss('div.type___2jLsS')
        for el in body_classes:
            body_class_text = el.text
            body_class_name = body_class_text.split(',')[0]
            assert body_class_name == search_filter

    def set_price_filter(self):
        s(by.text('Price')).click()
        s('.options___2FJcf.middleSize___2PoAB > .actions___1u4g_ > div > .buttonApply___2Pjua'). \
            should(be.enabled).click()

    def check_filtered_price_is_in_range(self, min_value, max_value):
        self.spinner.should_not(be.visible)
        prices = ss('span.price___DElEo')
        for el in prices:
            price_text = el.text
            price_value = int(price_text.split(' ')[1])
            assert price_value in range(min_value, max_value)
