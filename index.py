from selenium import webdriver
import time
import random
import string
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()


def fill_form(driver):
    fio = "testUser" + ''.join(random.choices(string.ascii_letters, k=5))
    phone = "+7999" + str(random.randint(1000000, 9999999))
    email = "test" + str(random.randint(1, 1000)) + "@example.com"
    password = "testpassword123"

    time.sleep(3)
    print('Заполняем имя')
    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys(fio)
    time.sleep(3)
    print('Заполняем телефон')
    phone_field = driver.find_element(By.NAME, "phone")
    phone_field.send_keys(phone)
    time.sleep(3)

    print('Заполняем email')
    email_field = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div[3]/div/form/div/div[3]/div[2]/input")
    email_field.send_keys(email)
    time.sleep(3)

    print('Заполняем пароль')
    pass1_field = driver.find_element(By.NAME, "pass1")
    pass1_field.send_keys(password)
    time.sleep(3)
    print('Подтверждаем пароль')
    pass2_field = driver.find_element(By.NAME, "pass2")
    pass2_field.send_keys(password)

    # Отмечаем чекбокс согласия
    print('Отмечаем чекбокс согласия')
    agreement_checkbox = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div[3]/div/form/div/div[6]/label/span[1]")
    agreement_checkbox.click()

    # Нажимаем кнопку "Зарегистрироваться"
    print('Нажимаем кнопку "Зарегистрироваться"')
    register_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div/div[2]/div[3]/div/form/div/div[7]/button")
    register_button.click()


driver = webdriver.Chrome(options=options)

driver.get("https://nashel.ru/")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[5]/div[1]/a[2]/span")
element.click()

time.sleep(3)

fill_form(driver)

time.sleep(5)

driver.quit()
