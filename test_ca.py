from playwright.sync_api import sync_playwright
import time

def test_get_my():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        browser.new_page()

def test_get_my(page):
    page.goto("https://www.gamestop.com")
        
    page.wait_for_selector("#subnav > li:nth-child(5) > a")
    page.click("#subnav > li:nth-child(5) > a")
    page.wait_for_selector("#subnav > li.show > ul > li:nth-child(1) > a")
    page.click("#subnav > li.show > ul > li:nth-child(1) > a")  
    time.sleep(5)

