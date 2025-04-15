from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Selectable.html')



    # 1. Mouse Actions
    # Hover over a menu item and confirm that a dropdown or tooltip appears.
    page.wait_for_selector('//a[text()="SwitchTo"]').hover()
    page.wait_for_timeout(2000)

    # Perform a single click on a visible button and verify the result.
    page.wait_for_selector('//a[contains(text(), "WebTable")]').click()
    page.wait_for_timeout(2000)

    # Perform a double-click on an element and check for expected changes.
    page.wait_for_selector('//a[text()="SwitchTo"]').dblclick()
    page.wait_for_timeout(3000)

    # Right-click on an element and validate the context menu or response.
    page.wait_for_selector('//a[text()="SwitchTo"]').click(button='right')
    page.wait_for_timeout(3000)

    page.wait_for_selector('//a[text()="SwitchTo"]').click(modifiers=["Shift"])
    page.wait_for_timeout(3000)


    #Keyboard Actions

    # Simulate typing a full sentence into a text input field.
    page.goto("https://demo.automationtesting.in/Register.html")
    page.fill("input[placeholder='First Name']", "Rutuja")
    page.fill("input[placeholder='Last Name']", "Nagdekar")

    # Press special keys like Enter, Tab, or symbols, and observe the effect.
    page.click("input[type='email']")
    page.keyboard.type('rsnagdekar@gmail.com')
    page.keyboard.press('Tab')
    page.keyboard.type('3323232323')
    page.wait_for_timeout(2000)
    # Navigate through items using arrow keys and confirm focus or selection behavior.
    #
    # Perform a Shift + Click action and verify multi-selection or special behavior.
    page.check("input[value='Movies']")
    page.check("input[value='Hockey']")
    page.wait_for_timeout(2000)

    # Use a keyboard shortcut (like Select All or Copy) and confirm the result.
    page.keyboard.press("Control+A")
    page.keyboard.press("Control+C")
    page.wait_for_timeout(2000)

    # Hover + Fill + Submit
    page.hover('//textarea[@ng-model="Adress"]')
    page.fill('//textarea[@ng-model="Adress"]' , "This is my new Address")
    page.wait_for_timeout(2000)

    #Submit form
    page.click('//button[@id = "submitbtn"]')


    # This is a practice Code

    # page.wait_for_selector('//a[text()="SwitchTo"]').press('A')
    # page.wait_for_timeout(3000)
    # #A-Z, 0-9, F1-F12, Special characters , ArrowRight, ArrowRight, Pageup, Enter, Control, Command
    # page.wait_for_selector('//a[text()="SwitchTo"]').press('$')
    page.wait_for_timeout(3000)