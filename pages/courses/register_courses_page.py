from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(RegisterCoursesPage, self).__init__(driver)
        self.driver = driver

    # Locators for elements
    _home_logo = "//div[@class='navbar-header']//a[@class='navbar-brand header-logo']" #xpath
    _search_box = "search-courses" #id
    _search_icon = "search-course-button" #id
    _course = "//div[@class='course-listing-title' and @title='{0}']" #xpath
    _all_courses = "//li/a[@href='/courses' and contains(text(), 'All Courses')]" #xpath
    _enroll_button = "enroll-button-top" #id
    # _use_another_card_button = "//button[contains(text(),'Use another card')]" #xpath
    # _cc_num = "cardnumber" #name
    # _cc_exp = "exp-date" #name
    # _cc_cvv = "cvc" #name
    # _cc_postal_code = "zipCode" #name
    _submit_enroll = "//span[contains(text(),'Buy Now')]" #xpath
    _enroll_error_message = "//li[contains(text(),'Sorry, there was an error completing your purchase')]" #xpath

    # Actions that are performed on locators
    def enterCourseName(self, courseName, testing):
        self.sendKeys(courseName, locator=self._search_box)
        self.elementClick(locator=self._search_icon)
        print(testing)

    def selectCourseToEnroll(self, courseName):
        self.elementClick(locator=self._course.format(courseName), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(locator=self._enroll_button)
    #
    # def enterCreditCardInformation(self, num, exp, cvv):
    #     pass

    def clickBuyNowButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def verifyEnrollmentFailed(self):
        result = self.isElementPresent(locator=self._enroll_error_message, locatorType="xpath")
        return result

    def goToHomePage(self):
        self.elementClick(locator=self._home_logo, locatorType="xpath")
