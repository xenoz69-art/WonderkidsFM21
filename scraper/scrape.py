from playwright.sync_api import sync_playwright

URL = "https://sortitoutsi.net/best-football-manager-2021-wonderkids"

requests_log = []


def log_request(request):
    requests_log.append({
        "method": request.method,
        "url": request.url,
        "resource": request.resource_type
    })


with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )

    page = browser.new_page()

    page.on("request", log_request)

    page.goto(URL, wait_until="domcontentloaded")

    page.wait_for_timeout(10000)

    browser.close()

print("===== REQUESTS =====")

for r in requests_log:
    print(f'{r["resource"]}  {r["method"]}  {r["url"]}')
