from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators



class TestConstructor:

    def test_navigation_by_bun(self, driver):
        driver.find_element(*PageLocators.BUTTON_TASTE).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.TEXT_TASTE))
        driver.find_element(*PageLocators.BUTTON_BUN).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.TEXT_BUN))
        assert driver.find_element(*PageLocators.BUTTON_BUN).text == "Булки"

    def test_navigation_by_sauce(self, driver):
        driver.find_element(*PageLocators.BUTTON_SAUCE).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.TEXT_BUN))
        assert driver.find_element(*PageLocators.TEXT_SAUCE).text == "Соусы"

    def test_navigation_by_taste(self, driver):
        driver.find_element(*PageLocators.BUTTON_TASTE).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.TEXT_TASTE))
        assert driver.find_element(*PageLocators.TEXT_TASTE).text == "Начинки"
