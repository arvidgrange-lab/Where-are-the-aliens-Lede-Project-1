import time
import pandas as pd
from playwright.sync_api import sync_playwright

TARGET_URL = "https://www.war.gov/UFO/limit/1000/?type=.pdf"
master_data = []

print("Booting the Chromium ghost engine...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print(f"Opening {TARGET_URL}...")
    page.goto(TARGET_URL)

    page.wait_for_load_state("networkidle")
    time.sleep(2)

    for current_page in range(1, 16):
        print(f"Scraping Page {current_page}...")

        # 1. SCRAPE YOUR SPECIFIC SPAN TAG
        page_data = page.locator(".record-meta").all_inner_texts()
        master_data.extend(page_data)

        if current_page == 15:
            break

        try:

            next_button = page.locator("button.pagination-next") 
            next_button.last.click() 
            page.wait_for_load_state("networkidle")
            time.sleep(2)

        except Exception as e:
            print(f"\nCRITICAL: Stopped early on page {current_page}. Error: {e}")
            break

    browser.close()

print(f"\nSuccess. Pulled {len(master_data)} total location records.")

df = pd.DataFrame(master_data)
df.to_csv("PURSUE_Locations.csv", index=False)
print("Saved to disk as: PURSUE_Locations.csv")