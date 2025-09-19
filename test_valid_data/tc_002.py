# TC-002:	Input all valid values to create a room record.
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationintesting.online/")
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_test_id("roomName").click()
    page.get_by_test_id("roomName").fill("101")
    page.locator("#accessible").select_option("true")
    page.locator("#roomPrice").click()
    page.locator("#roomPrice").fill("100")
    page.get_by_role("checkbox", name="WiFi").check()
    page.get_by_role("checkbox", name="TV").check()
    page.get_by_role("checkbox", name="Safe").check()
    page.get_by_role("button", name="Create").click()
    expect(page.locator("#room4")).to_contain_text("101")
    expect(page.locator("#room4")).to_contain_text("Single")
    expect(page.locator("#room4")).to_contain_text("true")
    expect(page.locator("#room4")).to_contain_text("100")
    expect(page.locator("#room4")).to_contain_text("WiFi, TV, Safe")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
