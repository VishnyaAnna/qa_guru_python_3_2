from selene.support.shared import browser
from selene.support.conditions import have


def test_google_search(open_browser):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_search_bad(open_browser):
    browser.element('[name=q]').type('hvkhgvbkubujgbhiljhbililhoiljh').press_enter()
    browser.element('[id=search]').should(have.text(
        "Your search - hvkhgvbkubujgbhiljhbililhoiljh - did not match any documents."))
