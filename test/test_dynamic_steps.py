import allure
from selene import browser, by, be

from test.test_decorator_steps import test_dynamic_label


def test_dinamic_steps():
    test_dynamic_label()
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").type("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Открываем репозиторий"):
        browser.element('a[href="/eroshenkoam/allure-example"]').click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issue c номер 84"):
        browser.element(by.partial_text("84")).should(be.visible)
