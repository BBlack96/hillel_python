import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
browser = browser.find_element(By.ID, 'answer')
browser.send_keys(y)
browser = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
browser.click()
browser = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
browser.click()
browser = browser.find_element(By.XPATH, "//*[@class='btn btn-default']")
browser.click()
time.sleep(5)