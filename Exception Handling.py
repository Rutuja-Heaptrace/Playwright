from lib2to3.fixes.fix_print import parend_expr
from logging import exception

from playwright.sync_api import sync_playwright

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://demo.automationtesting.in/Register.html')
        # Store multiple b elements
        elements = page.query_selector_all('a')  # 'b' for all b tags
        print(len(elements))

        for i in elements:
            #print(i.text_content())
            print(i.get_attribute('href'))

        page.wait_for_timeout(3000)
except Exception as e:
    print(str(e))

finally:
    print('This is a Finally Block')

