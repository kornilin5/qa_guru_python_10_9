import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity

from utils.fixture_steps import open_main_page, open_issue_tab, search_for_repository, go_to_repository, \
    should_see_issue_with_number


@allure.tag('Github')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'eroshenkoam')
@allure.feature("Tasks in repository")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')

    with allure.step("Ищем репозитория"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys(
            "eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)


@allure.tag('Github')
@allure.severity(Severity.MINOR)
@allure.label('Owner_2', 'eroshenkoam')
@allure.feature("Tasks in repository second variant")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")
