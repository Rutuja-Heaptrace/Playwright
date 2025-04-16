import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto('https://demo.automationtesting.in/Selectable.html')

        # 1. Mouse Actions
        # Hover over a menu item and confirm that a dropdown or tooltip appears.
        await page.locator('//a[text()="SwitchTo"]').hover()

        # Perform a single click on a visible button and verify the result.
        await page.locator('//a[contains(text(), "WebTable")]').click()

        # Perform a double-click on an element and check for expected changes.
        await page.locator('//a[text()="SwitchTo"]').dblclick()

        # Right-click on an element and validate the context menu or response.
        await page.locator('//a[text()="SwitchTo"]').click(button='right')

        # Perform a Shift + Click action and verify multi-selection or special behavior.
        await page.locator('//a[text()="SwitchTo"]').click(modifiers=["Shift"])

        # Keyboard Actions

        # Simulate typing a full sentence into a text input field.
        await page.goto("https://demo.automationtesting.in/Register.html")
        await page.fill("input[placeholder='First Name']", "Rutuja")
        await page.fill("input[placeholder='Last Name']", "Nagdekar")

        # Press special keys like Enter, Tab, or symbols, and observe the effect.
        await page.click("input[type='email']")
        await page.keyboard.type('rsnagdekar@gmail.com')
        await page.keyboard.press('Tab')
        await page.keyboard.type('3323232323')

        # Perform a Shift + Click action and verify multi-selection or special behavior.
        await page.check("input[value='Movies']")
        await page.check("input[value='Hockey']")

        # Use a keyboard shortcut (like Select All or Copy) and confirm the result.
        await page.keyboard.press("Control+A")
        await page.keyboard.press("Control+C")

        # Hover + Fill + Submit
        await page.hover('//textarea[@ng-model="Adress"]')
        await page.fill('//textarea[@ng-model="Adress"]', "This is my new Address")

        # Submit form
        await page.click('//button[@id = "submitbtn"]')

        # This is a practice Code

        # await page.locator('//a[text()="SwitchTo"]').press('A')
        # await page.wait_for_timeout(3000)
        # # A-Z, 0-9, F1-F12, Special characters , ArrowRight, ArrowRight, Pageup, Enter, Control, Command
        # await page.locator('//a[text()="SwitchTo"]').press('$')
        await page.wait_for_timeout(3000)

# Run the async function
asyncio.run(run())
