from tkinter import Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 20 секунд, пока цена не станет 100$
    pr = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.XPATH, "//*[@id='price']"), "100")
    )

    # когда условие достигнуто жмём кнопку
    button = browser.find_element(By.XPATH, "//*[@id='book']")
    button.click()

    # вычисляем капчу
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    # вставляем ответ
    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button1 = browser.find_element(By.XPATH, '//*[@id="solve"]')
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка