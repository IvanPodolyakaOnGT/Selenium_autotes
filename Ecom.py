from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# обращается к указанному файлу и забирает ссылку на платежную форму
with open("C:\\project\\fixtures\\Link.txt", "r") as f:
    link = f.read()

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "CardNumber")
    input1.send_keys("5586200075269701")
    input2 = browser.find_element(By.XPATH, "//*[@name='date']")
    input2.send_keys("11/25")
    input3 = browser.find_element(By.XPATH, "//*[@name='CardCvv']")
    input3.send_keys("641")
    input4 = browser.find_element(By.XPATH, "//*[@name='CardHolder']")
    input4.send_keys("Q E")
    button = browser.find_element(By.XPATH, "//*[@type='submit']")
    button.click()
  
finally:
    # ожидание отправки запроса
    time.sleep(30)
    # закрытие браузера 
    browser.quit()

# пустая последняя строка нам нужна