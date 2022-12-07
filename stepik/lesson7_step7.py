import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/get_attribute.html")
finding = browser.find_element(By.XPATH, "//*[@id='treasure']")
answer = finding.get_attribute("valuex")
y = calc(answer)
browser = browser.find_element(By.XPATH, "//*[@id='answer']")
browser.send_keys(y)
browser = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
browser.click()
browser = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
browser.click()
browser = browser.find_element(By.XPATH, "//*[@class='btn btn-default']")
browser.click()
time.sleep(5)

