from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from traceback import print_stack


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                    self.screenshot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                self.screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### EXCEPTION OCCURRED")
            self.screenshot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        # Mark the result of the verification point in a test case
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the last/final result of the verification point in a test case.
        This needs to be called at least once in a test case.
        This should be final test status of the test case.
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True
