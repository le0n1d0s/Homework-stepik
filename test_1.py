from selenium import webdriver
import time
import unittest
import pytest


class Test_Registration1(unittest.TestCase):

    def test_reg(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome("C:/chromedriver.exe")
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Почта")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
        time.sleep(1)

                # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

                # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()


    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome("C:/chromedriver.exe")
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Почта")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
        time.sleep(1)

                # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

                # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
    # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()