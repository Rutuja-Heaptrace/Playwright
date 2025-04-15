from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()  #Context can store more than 2 tabs
    page = context.new_page()

    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_selector('//button[contains(text() , "    click   ")]').click()
    page.wait_for_timeout(3000)


    # How to find total pages
    total_pages = context.pages
    print(len(total_pages), type(total_pages))

    for i in total_pages:
        print(i)


    print(page.title())
    child_page = total_pages[1]  #total_pages[0] is parent
    # How to switch to new page

    child_page.bring_to_front()
    page.wait_for_timeout(3000)
    print(child_page.title())
    child_page.close()

    page.bring_to_front()       #To make page active and Focused
    page.wait_for_timeout(3000)
    browser.close()






