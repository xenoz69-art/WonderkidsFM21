from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

URL = "https://sortitoutsi.net/best-football-manager-2021-wonderkids"

players = []

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
    )

    page = browser.new_page()

    page.goto(URL, wait_until="domcontentloaded", timeout=120000)

page.wait_for_timeout(10000)

html = page.content()

with open("debug.html", "w", encoding="utf-8") as f:
    f.write(html)

page.screenshot(path="debug.png", full_page=True)
    soup = BeautifulSoup(page.content(), "lxml")

    table = soup.find("table")

    rows = table.find_all("tr")[1:]

    for row in rows:
        cols = row.find_all("td")

        if len(cols) < 9:
            continue

        players.append({
            "name": cols[0].get_text(" ", strip=True),
            "age": cols[1].get_text(strip=True),
            "position": cols[2].get_text(" ", strip=True),
            "wage": cols[3].get_text(strip=True),
            "value": cols[4].get_text(strip=True),
            "cost": cols[5].get_text(strip=True),
            "expires": cols[6].get_text(strip=True),
            "rating": cols[7].get_text(" ", strip=True),
            "potential": cols[8].get_text(" ", strip=True)
        })

    browser.close()

with open("players.json", "w", encoding="utf-8") as f:
    json.dump(players, f, ensure_ascii=False, indent=2)

print(f"Total pemain: {len(players)}")
