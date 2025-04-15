# Cache - Store data on browser
# cookies - Store data on browser and server also

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.redbus.in/')
    my_cookies = page.context.cookies()
    print(my_cookies)

    #Clear all cookies
    page.context.clear_cookies()

    new_cookie = {
        'name':'Rutuja' ,
        'udid': 'fsddsfsdf34234343'
    }

    #page.context.add_cookies([new_cookie])
    page.screenshot(path='test.png', full_page=True)
    page.wait_for_timeout(2000)