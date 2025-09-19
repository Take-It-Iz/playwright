# Book the room using the User page(API), and then check that the room is
# booked on the Admin page(API)
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationintesting.online/")
    page.locator("#navbarNav").get_by_role("link", name="Rooms").click()
    page.locator("div").filter(has_text=re.compile(
        r"^£225 per nightBook now$")).get_by_role("link").click()
    page.get_by_role("button", name="Reserve Now").click()
    page.get_by_role("textbox", name="Firstname").click()
    page.get_by_role("textbox", name="Firstname").fill("Some")
    page.get_by_role("textbox", name="Firstname").press("Tab")
    page.get_by_role("textbox", name="Lastname").fill("Body")
    page.get_by_role("textbox", name="Lastname").press("Tab")
    page.get_by_role("textbox", name="Email").fill("oncetoldme@mail.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Phone").fill("12345678901234")
    page.get_by_role("button", name="Reserve Now").click()
    page.get_by_role("link", name="Return home").click()
    page.get_by_role("link", name="Admin", exact=True).click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Messages").click()
    page.get_by_text("Some Body").click()
    expect(page.get_by_label("onRequestClose Example")).to_contain_text(
        "From: Some BodyPhone: 12345678901234Email: oncetoldme@mail.comYou have a new booking!You have a new booking from Some Body. They have booked a room for the following dates: 2025-09-20 to 2025-09-21Close")
    page.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
