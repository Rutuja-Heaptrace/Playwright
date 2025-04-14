from playwright.async_api import async_playwright

with async_playwright() as p:
    browser = p.chromium.launch(headless=False)
    #headless - means run in backend and don't show me
    page = browser.new_page()
    page.goto('https://www.heaptrace.com/')
    print('Browser Successfully Launched')
    print(page.title())
    page.wait_for_timeout(3000)
    browser.close()