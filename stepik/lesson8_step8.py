import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']").send_keys("Name")
browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']").send_keys("Surname")
browser.find_element(By.XPATH, "//input[@placeholder='Enter email']").send_keys("email@mail.ua")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element(By.XPATH, "//input[@id='file']").send_keys("D:\Games")
browser.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
time.sleep(5)
browser.quit()
