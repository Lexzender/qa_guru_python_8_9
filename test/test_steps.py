from selene import browser, by, be



def test_steps():
    browser.open("https://github.com")
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").type("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()
    browser.element('a[href="/eroshenkoam/allure-example"]').click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("84")).should(be.visible)
