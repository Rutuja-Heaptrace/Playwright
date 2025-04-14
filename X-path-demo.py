from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #*************X-path - Traverse between web elements*****************
    #Relative X-path
    #1]  Using attribute - These are attributes (class, id , type , input etc.) of any Web element
    # Syntax = //tagname[@attributename = 'value']
    username_element = page.wait_for_selector('//input[@name="username"]')
    username_element.type('Admin')
    password_element = page.wait_for_selector('//input[@placeholder="Password"]')
    password_element.type('admin123')
    login_element = page.wait_for_selector('//button[@type="submit"]')
    login_element.click()
    page.wait_for_timeout(3000)


    # 2] Using Text
    # Syntax - //tagname[text() = "text"]

    page.wait_for_selector('//p[text()="Forgot your password? "]').click()
    page.wait_for_timeout(3000)


    # contains
    # attributes = //tagname[contains(@attribute, "value")]
    # text = //tagname[contains(text() , "Forgot your password? ")]


    # starts-with  - //tagname[starts-with(@id , 'prasanth')]
    # ends-with  - //tagname[starts-with(@id , 'prasanth')]


    # Family
    # parent - //tagname[@id = "xy"]/parent::input[]
    # child - //tagname[@id = "xy"]/child::input[]
    # ancestor - above 3-4 parent
    # Sibling - //td[text()="Microsoft"]//following-sibling::td[2]      -- Accessing 2nd row number element


