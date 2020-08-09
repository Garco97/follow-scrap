import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
from types import SimpleNamespace

import threading
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")   
#chrome_options.add_argument("-headless") 
with open('credentials.json') as f:
  config = json.load(f)
  config = SimpleNamespace(**config)
def log_in(driver):
  driver.get('https://www.instagram.com/')
  time.sleep(2)
  name = driver.find_element_by_name("username")
  name.send_keys(config.user)
  password = driver.find_element_by_name("password")
  password.send_keys(config.password)
  log = driver.find_elements_by_class_name("sqdOP")[1]
  log.click()
  time.sleep(2)
  log = driver.find_elements_by_class_name("sqdOP")[1]
  log.click()
  time.sleep(2)
  log = driver.find_elements_by_class_name("aOOlW")[0]
  log.click()
  print("Logged")
def go():
  try:
    driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
    log_in(driver)
    log = driver.find_elements_by_class_name("sqdOP")[1]
    log.click()
    print("User")

    time.sleep(2)
    log = driver.find_elements_by_class_name("g47SY")[1]
    log.click()
    print("Followers")
    time.sleep(2)

    while(True):
      log = driver.find_elements_by_class_name("sqdOP")
      print(len(log))
      for i in range(4,len(log)):
        log[i].click()
      time.sleep(2)
  except:
    driver.close()
    go()
      


if __name__ == "__main__":
    go()