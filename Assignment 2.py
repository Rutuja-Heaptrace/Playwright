from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')

    # Filling the form
    page.fill('//input[@placeholder="First Name"]', "Rutuja")
    page.fill('//input[@placeholder="Last Name"]', "Nagdekar")
    page.fill('//input[@type="email"]', "rsnagdekar@gmail.com")
    page.wait_for_timeout(3000)

    # Drop-down using page.select_option()
    page.select_option('//select[@id="Skills"]', label='C++')
    page.wait_for_timeout(3000)

    # Check box and Radio Buttons

    # Create Radio Button
    radio_button = page.query_selector('//input[@value="FeMale"]')
    radio_button.click()
    # or radio_button.check()
    # OR page.check("input[value='Cricket']")

    if radio_button.is_checked():
        print('Radio-Passed')
    else:
        print('Failed')

    # For checkboxes
    check_box = page.query_selector('//input[@value="Cricket"]')
    check_box.click()
    page.wait_for_timeout(3000)

    if check_box.is_checked():
        print('Check-Passed')
    else:
        print('Failed')

    page.wait_for_timeout(3000)


