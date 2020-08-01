from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript Masterclass", "COURSE1"), ("Learn Python 3 from scratch", "COURSE2"))
    @unpack
    def test_invalidEnrollment(self, courseName, testing):
        self.rc.enterCourseName(courseName, testing)
        self.rc.selectCourseToEnroll(courseName)
        self.rc.clickEnrollButton()
        self.rc.clickBuyNowButton()
        result = self.rc.verifyEnrollmentFailed()
        self.ts.markFinal(testName="test_invalidEnrollment",
                          result=result,
                          resultMessage="verifyEnrollmentFailed")
        self.rc.goToHomePage()
