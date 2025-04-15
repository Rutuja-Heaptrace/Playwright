from playwright.sync_api import sync_playwright


text_list = []

def handle_dialog(dialog):
    text_list.append(dialog.message)
    dialog.accept()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')

    # //            //   - Can jump to any Generation
    # //            / - Can go to direct child

    #page.wait_for_selector('//div[@id="OKTab"]/button').click()
    page.wait_for_selector('//a[@href="#CancelTab"]').click()
    page.wait_for_timeout(3000)

    # Control alert
    #page.on("dialog", lambda dialog : dialog.accept())   # Accept Dialog Box
    #page.on("dialog", lambda dialog : dialog.dismiss())   #// Dismiss Dialog Box


    # page.on("dialog", lambda dialog : dialog.accept())  # // Dismiss Dialog Box
    page.on("dialog", handle_dialog)  # Custom Functins


    # In Playwright, the page.on() method is used to listen for events
    # that occur on a web page—such as when a request is made,
    # a response is received, a dialog pops up

    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    print(text_list)
    page.wait_for_timeout(3000)

