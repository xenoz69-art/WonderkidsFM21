from playwright.sync_api import sync_playwright

URL = "https://sortitoutsi.net/best-football-manager-2021-wonderkids"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=120000)

    print("Title :", page.title())

    page.screenshot(path="page.png", full_page=True)

    html = page.content()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(html)

    browser.close()

print("Selesai")
