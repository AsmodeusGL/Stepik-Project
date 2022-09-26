import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', default='en', help="Choose language: en, es, fr or others")


@pytest.fixture(scope="class")
def browser(request):
    page_language = request.config.getoption('language')
    match page_language:
        case 'es':
            print('\nBrowser launched on Spanish language\n')
        case 'en':
            print('\nBrowser launched on English language\n')
        case 'fr':
            print('\nBrowser launched on French language\n')
        case _:
            print(f'\nBrowser launched on {page_language} language\n')

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': page_language})

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    yield browser

    print("\nQuit browser ...")

    browser.quit()
