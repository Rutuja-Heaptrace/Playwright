import asyncio
from playwright.async_api import async_playwright

#Reusable Function
async def get_texts_by_selector(page, selector: str) -> list:
    try:
        # Wait for the selector to appear
        await page.wait_for_selector(selector, timeout=5000)
        elements = await page.query_selector_all(selector)
        texts = [await element.text_content() for element in elements]
        cleaned_texts = [text.strip() for text in texts if text]
        assert cleaned_texts, f"No elements found for selector: {selector}"
        return cleaned_texts
    except Exception as e:
        print(f"[ERROR] Failed to extract {selector}")
        return []


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        #Go to Register URL
        await page.goto("https://demo.automationtesting.in/Register.html")

        #Extract text from Label Tags
        print("\n *********Printing label tag texts:**************")
        label_texts = await get_texts_by_selector(page, "label")
        for text in label_texts:
            print(text)

        # Extract href attribute from 'a' tag
        print("\n ************<a> tag hrefs:**************")
        hrefs = []
        try:
            a = await page.query_selector_all('a')
            for i in a:
                if i is not None:
                # print(i.text_content())
                    h= await i.get_attribute('href')
                    hrefs.append(h)

            # Assertion added to validate extracted elements
            assert hrefs, "No hrefs found in <a> tags"

            for href in hrefs:
                print("*", href)
        except Exception as e:
            print("[ERROR] Failed to extract <a> hrefs:", e)

        #Navigate multiple pages to extract tags
        print('\n**********Navigating to different sites and extract elements************')
        pages_to_visit = [
            ("https://demo.automationtesting.in/WebTable.html", "h1"),
            ("https://demo.automationtesting.in/Alerts.html", "h2"),
            ("https://demo.automationtesting.in/Datepicker.html", "h4")
        ]

        texts=[]
        for url, selector in pages_to_visit:
            print(f"\nNavigating to: {url}")
            await page.goto(url)
            try:
                text= await get_texts_by_selector(page, selector)
                print(text)
            except:
                print("No text found.")

        await browser.close()


asyncio.run(main())
