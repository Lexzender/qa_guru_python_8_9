import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Kostromin")
@allure.feature("Репозиторий")
@allure.story("Проверка отображения Issue")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository('a[href="/eroshenkoam/allure-example"]')
    open_issue_tab()
    should_see_issue_with_number("84")


def test_dynamic_label():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Репозиторий")
    allure.dynamic.story("Проверка отображения Issue")
    allure.dynamic.link("https://github.com", name="Testing")
    allure.dynamic.label("owner", "Kostromin")


@allure.step("Открыть главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(repo).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
