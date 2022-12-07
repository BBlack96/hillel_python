import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x)+int(y))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element(By.XPATH, "//span[@id='num1']").text
y = browser.find_element(By.XPATH, "//span[@id='num2']").text
result = calc(x, y)
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(result)
browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
time.sleep(5)
browser.quit()
