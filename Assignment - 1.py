import asyncio
from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Use True for headless mode
        context = await browser.new_context()
        page = await context.new_page()


        # Step 1: Open the URL
        await page.goto("https://www.saucedemo.com/", timeout=10000)
        await page.wait_for_timeout(3000)

        # Step 2: Fill the login form using CSS and XPath selectors
        await page.fill('input[data-test="username"]', "standard_user")  # CSS selector
        await page.fill('//input[@data-test="password"]', "secret_sauce")  # XPath selector
        await page.wait_for_timeout(2000)

        # Step 3: Click login button
        await page.click('input[data-test="login-button"]')
        await page.wait_for_timeout(2000)

        # Step 4: Wait for products page to load using wait_for_selector with custom timeout
        await page.wait_for_selector('.inventory_list', timeout=5000)
        await page.wait_for_timeout(2000)

        # Step 5: Extract text of first product title
        # Here page.inner_text returns only first match
        first_product_title = await page.inner_text('.inventory_item_name')
        print("First product title:", first_product_title)
        await page.wait_for_timeout(2000)

        # Step 6: Navigate to product details page
        await page.click('.inventory_item_name')
        await page.wait_for_selector('.inventory_details_name', timeout=3000)
        await page.wait_for_timeout(2000)

        # Step 7: Extract and assert product name on detail page
        product_name = await page.inner_text('.inventory_details_name')
        assert product_name == first_product_title, "Product name mismatch!"
        await page.wait_for_timeout(2000)

        # Step 8: Go back to products page
        await page.goto("https://www.saucedemo.com/inventory.html")
        await page.wait_for_timeout(2000)

        # Final Assertion: Check if logout button is visible in menu
        await page.click('#react-burger-menu-btn')
        await page.wait_for_selector('#logout_sidebar_link', timeout=3000)
        logout_text = await page.inner_text('#logout_sidebar_link')
        assert logout_text.lower() == "logout", "Logout link not found!"
        await page.wait_for_timeout(2000)

        print("All steps passed successfully.")

        await browser.close()

# Run the async function
asyncio.run(run_test())
