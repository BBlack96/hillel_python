import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://metanit.com/java/tutorial/1.1.php"
browser = webdriver.Chrome()
browser.get(link)
browser.execute_script("document.title='Script executing';alert('Robots at work');") #
time.sleep(5)
browser.quit()
