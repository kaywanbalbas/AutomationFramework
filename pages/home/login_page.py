from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # Calls the __init__ method of the parent aka super class becuase
        #   it also needs the driver instance to perform actions on elements
        super(LoginPage, self).__init__(driver)
        self.driver = driver

    # Locators for elements
    # IMPORTANT: If locator ID/NAME/CLASSES etc change on website, make changes here!
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # Actions that are performed on locators
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def clearLoginFields(self):
        self.clearField(self._email_field)
        self.clearField(self._password_field)

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearLoginFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[contains(@class,'open-my-profile-dropdown')]",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        if "Let's Kode It" in self.getTitle():
            return True
        else:
            return False
