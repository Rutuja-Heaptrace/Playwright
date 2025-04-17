from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #1. Log all AJAX requests
    def log_ajax(request):
        if request.resource_type == "xhr" or "ajax":
            print(f"AJAX Request: {request.method} {request.url}")

    page.on("request", log_ajax)


    #3. Navigate to the page
    page.goto("https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php")
    select = page.wait_for_selector('//select[@id="s1"]')

    select.select_option('2')


    page.wait_for_timeout(2000)
    browser.close()


