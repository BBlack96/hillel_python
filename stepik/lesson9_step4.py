from lesson7_step5 import calc
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.XPATH, "//button[normalize-space()='I want to go on a magical journey!']").click()
confirm = browser.switch_to.alert.accept()
x = browser.find_element(By.XPATH, "//span[@id='input_value']").text
result = calc(x)
browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result)
browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
print(browser.switch_to.alert.text)
