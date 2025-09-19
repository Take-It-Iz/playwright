# Create a Room using the Admin page(API) and check that the room was created
# on the User page(API)
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
    page.get_by_test_id("roomName").fill("42")
    page.locator("#accessible").select_option("true")
    page.locator("#roomPrice").click()
    page.locator("#roomPrice").fill("666")
    page.get_by_role("checkbox", name="WiFi").check()
    page.get_by_role("checkbox", name="TV").check()
    page.get_by_role("checkbox", name="Radio").check()
    page.get_by_role("button", name="Create").click()
    page.get_by_role("link", name="Front Page").click()
    page.locator("#navbarNav").get_by_role("link", name="Rooms").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
