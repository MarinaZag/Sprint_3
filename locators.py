from selenium.webdriver.common.by import By


class PageLocators:
    # Локаторы для проверки регистрации
    NAME_INPUT_REG = By.XPATH, './/label[text()="Имя"]/following-sibling::input' #поле для ввода имени
    EMAIL_INPUT_REG = By.XPATH, './/label[text()="Email"]/following-sibling::input' #поле для ввода почты
    PASSWORD_INPUT_REG = By.XPATH, './/input[(@name="Пароль")]' #поле для ввода пароля
    REG_BUTTON = By.XPATH, './/button[text()="Зарегистрироваться"]' #кнопка регистрации
    PASSWORD_ERROR_REG = By.XPATH, './/*[text()="Некорректный пароль"]' #подсказка о неккоректном пароле
    LINK_REG = By.XPATH, './/*[text()="Зарегистрироваться"]' #кнопка ссылка зарегестрироваться
    HEADING_REG = (By.XPATH, '//h2') #заголовок Зарегистрироваться
    # Локаторы для проверки авторизации
    EMAIL_INPUT_LOGIN = By.XPATH, './/label[text()="Email"]/following-sibling::input' #поля для ввода почты
    PASSWORD_INPUT_LOGIN = By.XPATH, './/input[(@name="Пароль")]'  # поле для ввода пароля
    BUTTON_ENTER = By.XPATH, './/button[text()="Войти"]' #кнопка входа
    BUTTON_LOGIN_ACCOUNT = By.XPATH, './/button[contains(text(),"Войти в аккаунт")]'  # кнопка войти в аккаунт
    LINK_RESTORE_PASSWORD = By.XPATH, './/*[text()="Восстановить пароль"]' #кнопка для восстановления пароля
    BUTTON_ORDER = By.XPATH, './/button[text()="Оформить заказ"]' #кнопка заказа
    HEADING_ENTER = By.XPATH, '//h2' #Заголовок "Вход"
    BUTTON_RESTORE_PASS = By.XPATH, './/*[text()="Восстановить"]' #кнопка восстановления пароля
    LINK_ENTER = By.XPATH, "//a[contains(text(), 'Войти')]" #кнопка-ссылка Войти
    # Локаторы для проверки выхода из профиля
    BUTTON_LOGOUT = By.XPATH, './/button[text()="Выход"]' #кнопка выхода
    PROFILE_LINK = By.XPATH, './/p[text()="Личный Кабинет"]' #Личный Кабинет
    # Локаторы для проверки переходов
    CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]' #кнопка перехода к конструктору
    LOGO = By.CLASS_NAME, 'AppHeader_header__logo__2D0X2' #логотип
    COLLECT_BURGER = By.XPATH, '//h1[text()="Соберите бургер"]' #заголовок "Соберите бургер"
    PROFILE = By.XPATH, '//a[text()="Профиль"]' #кнопка ссылка Профиль
    # Локаторы проверки переходов к разделам
    BUTTON_BUN = By.XPATH, '//span[text() = "Булки"]' #вкладка булок
    TEXT_BUN = By.XPATH, './/h2[text()="Булки"]' #раздел булок
    BUTTON_SAUCE = By.XPATH, '//span[text()="Соусы"]' #вкладка соусов
    TEXT_SAUCE = By.XPATH, './/h2[text()="Соусы"]'  # раздел соусов
    BUTTON_TASTE = By.XPATH, '//span[text()="Начинки"]' #вкладка начинок
    TEXT_TASTE = By.XPATH, './/h2[text()="Начинки"]' #раздел начинок





