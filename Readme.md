=======

Tests are built with help of:
 * Framework [Selene](https://github.com/yashaka/selene) (python selenium wrapper)
 * Page Object Model
 * Framework [Pytest](https://docs.pytest.org/en/latest/)

# Precondition

* [Python 3+](https://www.python.org/) and built in manager pip3
* Latest [Chrome](https://www.google.com/chrome/) Browser
* Latest [ChromeDriver](https://chromedriver.storage.googleapis.com/index.html) for Chrome installed in PATH


# Installation

Install dependencies `pip3 install -r requirements.txt`

# Start tests

Linux example
```
$ pytest test_search_filters.py
```

Same for Windows

# Tests description

* test_body_style_filters  
Here we set each body filter and check that in results we see only campers by chosen filter

* test_price_filter  
Here we set price range and check that in results price is in range of the chosen filter

* test_body_style_and_price_filter  
Here we combine both above filters and check that results are correct