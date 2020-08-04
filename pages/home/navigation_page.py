from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # Calls the __init__ method of the parent aka super class because
        #   it also needs the driver instance to perform actions on elements
        super(NavigationPage, self).__init__(driver)
        self.driver = driver

    # Locators for elements
    # IMPORTANT: If locator ID/NAME/CLASSES etc change on website, make changes here!
    _home_logo = "//div[@class='navbar-header']//a[@class='navbar-brand header-logo']"  #xpath
    _my_courses = "My Courses"  #link
    _all_courses = "All Courses"  #link
    _practice = "Practice"  #link
    _user_icon = "//a[contains(@class,'open-my-profile-dropdown')]"  #xpath
    # _user_icon = "//div[@id='navbar']//li[@class='dropdown']" #xpath


    # Actions that are performed on locators
    def navigateToHome(self):
        self.elementClick(locator=self._home_logo, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_icon, locatorType="xpath",
                                                  pollFrequency=1)
        self.elementClick(element=userSettingsElement)

    # def clickLoginLink(self):
    #     self.elementClick(self._login_link, locatorType="link")
    #
    # def enterEmail(self, email):
    #     self.sendKeys(email, self._email_field)
    #
    # def enterPassword(self, password):
    #     self.sendKeys(password, self._password_field)
    #
    # def clickLoginButton(self):
    #     self.elementClick(self._login_button, locatorType="name")
    #
    # def clearLoginFields(self):
    #     self.clearField(self._email_field)
    #     self.clearField(self._password_field)
    #
    # def login(self, email="", password=""):
    #     self.clickLoginLink()
    #     self.clearLoginFields()
    #     self.enterEmail(email)
    #     self.enterPassword(password)
    #     time.sleep(2)
    #     self.clickLoginButton()
    #
    # def verifyLoginSuccessful(self):
    #     result = self.isElementPresent("//a[contains(@class,'open-my-profile-dropdown')]",
    #                                    locatorType="xpath")
    #     return result
    #
    # def verifyLoginFailed(self):
    #     result = self.isElementPresent("//div[contains(text(), 'Invalid email or password.')]",
    #                                    locatorType="xpath")
    #     return result
    #
    # def verifyLoginTitle(self):
    #     return self.verifyPageTitle("Let's Kode It")
