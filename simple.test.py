import selene
from selene import browser
from selene.support.conditions import have

browser.open_url('http://google.com/ncr')
browser.element('[name=q]').type('selene').press_enter()
browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


