import re
from playwright.sync_api import Page, expect
from resources.wikipedia import urls, welkomsttekst, zoekveld, zoekknop, titeltekst, welkomsttekst_tikfout


def test_checks_that_i_can_visit_wikipedia(page: Page):
    page.goto(urls["basic_url"])
    expect(page).to_have_title(re.compile("Wikipedia"))


def test_checks_that_i_can_find_the_platypus_page_on_the_english_wikipedia(page: Page):
    # go to the English Wikipedia page
    page.goto(urls["english_url"])
    # checks that the page is in English
    expect(page.locator(welkomsttekst)).to_contain_text("Welcome to")
    # search for the Platypus
    page.locator(zoekveld).fill("Platypus")
    page.locator(zoekknop).click()
    # check that the Platypus page was found
    expect(page.locator(titeltekst)).to_be_visible()
    expect(page.locator(titeltekst)).to_have_text("Platypus")


def test_fails_on_purpose(page: Page):
    # go to the English Wikipedia page
    page.goto(urls["english_url"])
    # checks that the page is in English
    expect(page.locator(welkomsttekst_tikfout)).to_contain_text("Welcome to")
    # search for the Platypus
    page.locator(zoekveld).fill("Platypus")
    page.locator(zoekknop).click()
    # check that the Platypus page was found
    expect(page.locator(titeltekst)).to_be_visible()
    expect(page.locator(titeltekst)).to_have_text("Platypus")
