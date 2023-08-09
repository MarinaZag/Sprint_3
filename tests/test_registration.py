from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from faker import Faker

fake = Faker()
def generate():
    name = fake.name()
    email = fake.email()
    password = fake.password(length=6)
    return name, email, password

class TestRegistration:
    def test_registration_with_correct_password(self, driver):
        name, email, password = generate()
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.LINK_REG).click()
        driver.find_element(*PageLocators.NAME_INPUT_REG).send_keys(name)
        driver.find_element(*PageLocators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_REG).send_keys(password)
        driver.find_element(*PageLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.HEADING_ENTER))
        assert driver.find_element(*PageLocators.HEADING_ENTER).text == "Вход"

    def test_registration_with_incorrect_password(self, driver):
        name, email, password = generate()
        driver.find_element(*PageLocators.PROFILE_LINK).click()
        driver.find_element(*PageLocators.LINK_REG).click()
        driver.find_element(*PageLocators.NAME_INPUT_REG).send_keys(name)
        driver.find_element(*PageLocators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_REG).send_keys(password[:5])
        driver.find_element(*PageLocators.REG_BUTTON).click()
        WebDriverWait(driver, 3). \
            until(EC.visibility_of_element_located(PageLocators.PASSWORD_ERROR_REG))
        assert driver.find_element(*PageLocators.PASSWORD_ERROR_REG).text == "Некорректный пароль"
