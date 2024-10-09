# теория

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(
        By.CSS_SELECTOR,
        "body > div > form > div.first_block > div.form-group.first_class > input",
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR,
        "body > div > form > div.first_block > div.form-group.second_class > input",
    )
    input2.send_keys("Petrov")
    input3 = browser.find_element(
        By.CSS_SELECTOR,
        "body > div > form > div.first_block > div.form-group.third_class > input",
    )
    input3.send_keys("example@example.com")
    input4 = browser.find_element(
        By.CSS_SELECTOR,
        "body > div > form > div.second_block > div.form-group.first_class > input",
    )
    input4.send_keys("8-800-555-55-55")
    input5 = browser.find_element(
        By.CSS_SELECTOR,
        "body > div > form > div.second_block > div.form-group.second_class > input",
    )
    input5.send_keys("Россия, Санкт-Петербург, Басеенная, 38")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание
    time.sleep(10)
    # закрываем браузер
    browser.quit()

# пустая строка в конце файла
