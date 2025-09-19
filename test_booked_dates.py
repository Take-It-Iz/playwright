# TC-S001: Check the earlier booked dates status
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationintesting.online/")
    page.locator("div").filter(has_text=re.compile(
        r"^Check In$")).get_by_role("textbox").click()
    page.get_by_role("button", name="Previous Month").dblclick()
    page.get_by_role("option", name="Choose Friday, 20 June").click()
    page.locator("div").filter(has_text=re.compile(
        r"^Check Out$")).get_by_role("textbox").click()
    page.get_by_role("button", name="Previous Month").dblclick()
    page.get_by_role("button", name="Previous Month").click()
    page.get_by_role("option", name="Choose Friday, 27 June").click()
    page.get_by_role("button", name="Check Availability").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
