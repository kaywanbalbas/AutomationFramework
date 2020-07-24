from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenShotDirectory = "../screenshots/"
        relativeFileName = screenShotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenShotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("### EXCEPTION OCCURRED")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("getElement Element Found with locator: " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element Not Found with locator: " + locator +
                          " and locatorType: " + locatorType)
        return element

    def getElementsList(self, locator, locatorType="id"):
        elementList = []
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            elementList = self.driver.find_elements(byType, locator)
            self.log.info("List of Elements Found")
        except:
            self.log.info("List of Elements Not Found")
        return elementList

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("isElementPresent Element Found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element Not Found with locator: " + locator +
                              " and locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element Not Found with locator: " + locator +
                          " and locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element Not Found")
                return False
        except:
            self.log.info("Element Not Found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " +
                          str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, 1,
                                 [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))

            self.log.info("Element appeared on the page")
        except:
            self.log.info("Element did not appear on the page")
            print_stack()
        return element

    def clearField(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Cleared text for element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear text for element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()
