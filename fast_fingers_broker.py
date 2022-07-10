'''
The timer starts after the first keypress, so everything done before it doesn't count.
The second word needed to be typed after a delay.
I didn't want to put any test inside the typing loop.
You can type two words at once.

(for "not me" readers)
    Hello, world!
    It wasn't serious and I could probably do it faster with some research.
'''

from time import sleep
from playwright.sync_api import sync_playwright
import variables as var


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto(var.TEXT_SLUG_LINK, timeout=60000)

    # page.locator(var.DENY_BUTTON_XPATH).click()
    # I suggest you to click manually.


    page.locator(var.TEXT_INPUT_XPATH).click()

    xpath = var.GENERIC_XPATH
    text = page.locator(xpath).inner_text()
    word = ['', text]

    for i in range(2, 1906):
        xpath = f'xpath=//*[@id="row1"]/span[{i}]'
        word.append(page.locator(xpath).inner_text())

    page.keyboard.type(text)
    page.keyboard.type(' ')
    sleep(0.5)

    for i in range(1906, 1906+5):
        word.append('padding')

    for i in range(3, 1906, 2):
        text = word[i] + ' ' + word[i+1]
        page.keyboard.type(text)
        page.keyboard.type(' ')
    sleep(120)
