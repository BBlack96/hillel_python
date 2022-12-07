import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from math_function import calc


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.XPATH, "//button[normalize-space()='I want to go on a magical journey!']").click()
new_tab = browser.window_handles[1]
browser.switch_to.window(new_tab)
time.sleep(1)
x = browser.find_element(By.ID, "input_value").text
result = calc(x)
browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result)
browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
alert = browser.switch_to.alert.text
print(alert)