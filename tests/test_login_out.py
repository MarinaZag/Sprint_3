from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators


class TestLogout:

    def test_login_out(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_ORDER))
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_LOGOUT))
        driver.find_element(*PageLocators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_ENTER))
        assert driver.find_element(*PageLocators.HEADING_ENTER).text == "Вход"
