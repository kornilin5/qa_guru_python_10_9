import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://github.com')

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys(
        "eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
