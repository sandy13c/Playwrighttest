import unittest
from playwright.sync_api import sync_playwright
import time
class TestExample(unittest.TestCase):
    def setUp(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def test_title(self):
        self.page.goto("https://gamestop.com")
        #self.assertIn("GameStop", self.page.title())
        self.page.click("#subnav > li:nth-child(4) > a")
        self.page.click("#subnav > li.show > ul > li:nth-child(5) > a")
        time.sleep(15)
        # self.page.wait_for_timeout(6700)

    def testmyone(self): 
        self.page.goto("https://ezaudit.ed.gov/EZWebApp/default.do")
        
        # Click on the button
        self.page.click("table tr:nth-of-type(5) td:nth-of-type(2) button")
        
        # Enter username
        self.page.fill("form table:nth-of-type(2) tr:nth-of-type(3) input", "pfix02")
        
        # Enter password
        self.page.fill("form table:nth-of-type(2) tr:nth-of-type(4) input", "ProdProd!23456@8!1")
        
        # Click on the login button
        self.page.click("form table:nth-of-type(2) tr:nth-of-type(5) a img")
        
        # Click on another link or button
        self.page.click("body > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr > td > a:nth-child(7) > img")
        self.page.locator("select[name='ins_type']").select_option("Public")
        self.click("body > a:nth-child(3) > table:nth-child(5) > tbody > tr:nth-child(1) > td:nth-child(2) > form > table > tbody > tr:nth-child(43) > td > a > img")

        time.sleep(30)


if __name__ == "__main__":
    unittest.main()
