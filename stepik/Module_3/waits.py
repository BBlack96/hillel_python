import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math_function import calc


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.maximize_window()
amount = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100"))
button = browser.find_element(By.ID, "book").click()
x = browser.find_element(By.ID, "input_value").text
result = calc(x)
browser.find_element(By.ID, "answer").send_keys(result)
browser.find_element(By.ID, "solve").click()

