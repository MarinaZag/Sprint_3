from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators


class TestLogin:

    def test_login_by_account_button(self, driver):
        driver.find_element(*PageLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(*PageLocators.HEADING_ENTER))
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_ORDER))
        assert driver.find_element(*PageLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_by_link(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_ENTER))
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_ORDER))
        assert driver.find_element(*PageLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_by_restore_password(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.LINK_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_RESTORE_PASS))
        driver.find_element(*PageLocators.LINK_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_ENTER))
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_ORDER))
        assert driver.find_element(*PageLocators.BUTTON_ORDER).text == "Оформить заказ"

    def test_login_by_menu_registration(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_REG))
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_ENTER))
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.BUTTON_ORDER))
        assert driver.find_element(*PageLocators.BUTTON_ORDER).text == "Оформить заказ"