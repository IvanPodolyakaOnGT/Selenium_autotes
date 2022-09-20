from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//*[@id='num1']")
    x = x_element.text
    y_element = browser.find_element(By.XPATH, "//*[@id='num2']")
    y = y_element.text
    n = str(int(x) + int(y))

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.XPATH, "//*[@id='dropdown']"))
    select.select_by_value(n) 

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка