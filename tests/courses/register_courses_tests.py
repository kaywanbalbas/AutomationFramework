from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.rc.enterCourseName("JavaScript")
        self.rc.selectCourseToEnroll("559180")
        self.rc.clickEnrollButton()
        self.rc.clickBuyNowButton()
        result = self.rc.verifyEnrollmentFailed()
        self.ts.markFinal(testName="test_invalidEnrollment",
                          result=result,
                          resultMessage="verifyEnrollmentFailed")
