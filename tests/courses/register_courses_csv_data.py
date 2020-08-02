from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage
import unittest
import pytest
from ddt import ddt, data, unpack
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/K1/Documents/python_workspace/AutomationFramework/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, courseCount):
        self.rc.enterCourseName(courseName, courseCount)
        time.sleep(1)
        self.rc.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.rc.clickEnrollButton()
        self.rc.clickBuyNowButton()
        time.sleep(1)
        result = self.rc.verifyEnrollmentFailed()
        self.ts.markFinal(testName="test_invalidEnrollment",
                          result=result,
                          resultMessage="verifyEnrollmentFailed")
