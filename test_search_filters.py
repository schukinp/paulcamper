import pytest
from rent_camper_page import RentCamperPage
from data import body_style_options


@pytest.mark.usefixtures('setup')
class TestFilters(object):
    @pytest.mark.parametrize('search_filter', body_style_options)
    # set body_style filter and check only these types of body_styles are displayed in results
    def test_body_style_filters(self, search_filter):
        RentCamperPage().open_base_url()
        RentCamperPage().set_body_style_filter(search_filter)
        RentCamperPage().check_body_style_is(search_filter)

    def test_price_filter(self):
        # set price range filter and check the price is in range from 30 to 180
        RentCamperPage().open_base_url()
        RentCamperPage().set_price_filter()
        RentCamperPage().check_filtered_price_is_in_range(30,180)

    def test_body_style_and_price_filter(self):
        # combine both above filters and check the results
        RentCamperPage().open_base_url()
        RentCamperPage().set_price_filter()
        RentCamperPage().set_body_style_filter('Camper bus')
        RentCamperPage().check_filtered_price_is_in_range(30,180)
        RentCamperPage().check_body_style_is('Camper bus')
