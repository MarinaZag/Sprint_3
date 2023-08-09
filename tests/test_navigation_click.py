from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators


class TestNavigationClick:

    def test_entry_by_login_form(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.PROFILE))
        assert driver.find_element(*PageLocators.PROFILE).text == "Профиль"

    def test_entry_by_click_constructor(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.PROFILE))
        driver.find_element(*PageLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.COLLECT_BURGER))
        assert driver.find_element(*PageLocators.COLLECT_BURGER).text == "Соберите бургер"

    def test_entry_by_click_logo(self, driver):
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.EMAIL_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.PASSWORD_INPUT_LOGIN).send_keys("agata@yandex.ru")
        driver.find_element(*PageLocators.BUTTON_ENTER).click()
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.PROFILE))
        driver.find_element(*PageLocators.LOGO).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.COLLECT_BURGER))
        assert driver.find_element(*PageLocators.COLLECT_BURGER).text == "Соберите бургер"
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(*PageLocators.PROFILE))
        driver.find_element(*PageLocators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.COLLECT_BURGER))
        assert driver.find_element(*PageLocators.COLLECT_BURGER).text == "Соберите бургер"
