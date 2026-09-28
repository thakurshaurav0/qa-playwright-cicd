from playwright.sync_api import sync_playwright


def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto("https://webmail.suramicro.systems/")

        page.get_by_label("Email Address").fill("YOUR_EMAIL")
        page.get_by_text("Password", exact=True).fill("YOUR_PASSWORD")

        page.get_by_role("button", name="Log in").click()

        print("Login Completed")

        page.wait_for_timeout(5000)

        browser.close()