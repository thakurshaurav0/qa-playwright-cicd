import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://webmail.suramicro.systems/")
    page.get_by_label("Email Address").fill('shaurav.thakur@suramicro.systems')
    page.get_by_text("Password", exact=True).fill('Thakur@4119')
    page.get_by_role("button", name="Log in").click()
    print('Login Completed')

    page.wait_for_timeout(15000)
    print('Browser waited for 15 seconds')
    browser.close()