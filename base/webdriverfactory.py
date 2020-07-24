from selenium import webdriver

"""
@package base

WebDriverFactory class implementation:
This class creates a webdriver instance based on browser parameter

Example:
    wdf = WebDriveryFactory(browser)
    wdf.getWebDriverInstance()
    
IMPORTANT: Paths to driver files must already be set or defined
"""


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        if self.browser == "chrome":
            opt = webdriver.ChromeOptions()
            opt.add_argument("user-data-dir=/Users/K1/Library/Application Support/Google/Chrome/Default")
            driver = webdriver.Chrome(options=opt)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        else:
            opt = webdriver.ChromeOptions()
            opt.add_argument("user-data-dir=/Users/K1/Library/Application Support/Google/Chrome/Default")
            driver = webdriver.Chrome(options=opt)

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        return driver
