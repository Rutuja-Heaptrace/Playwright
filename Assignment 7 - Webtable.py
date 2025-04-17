from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')
    table = page.wait_for_selector('//table[@id="customers"]')

    tr = table.query_selector_all('tr')
    print('Total rows:' ,len(tr))

    td = table.query_selector_all('td')
    print('Total data cells: ' ,len(td))

    ls = []

    for row in tr:
        dt={}
        cells = row.query_selector_all('td')

        # Converting
        for index , cell in enumerate(cells, start=1):
            dt[index]=cell.text_content()
        ls.append(dt)

    print('List of Dictionaries' , ls)

    list_of_ones = [d[1]for d in ls if 1 in d]
    print(list_of_ones)
    page.wait_for_timeout(2000)


    # Data is sorted using key-1
    sorted_data = sorted(ls, key=lambda x: x.get(1, ''))
    print(sorted_data)

    # Storing file as CSV
    with open('webtable.json' , 'w') as f:
        json.dump(ls , f)