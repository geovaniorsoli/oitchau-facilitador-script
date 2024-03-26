import time
import os 
from selenium import webdriver
import ctypes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# dotenv environment
import os 
from dotenv import load_dotenv
load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASS")
web = os.getenv("WEB")

driver = webdriver.Edge()

try:
    driver.execute_script("window.open('about:blank', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(web) 

    inputs = WebDriverWait(driver, 9000).until(EC.visibility_of_all_elements_located((By.NAME, "email")))
    password_input = WebDriverWait(driver, 9000).until(EC.visibility_of_element_located((By.NAME, "password")))
    
    inputs[0].send_keys(user)
    password_input.send_keys(password)
    
    button = WebDriverWait(driver, 9000).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Acessar painel')]")))
    button.click()

    button = WebDriverWait(driver, 9000).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Marcar Ponto')]")))
    button.click()
    
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'MARCAR PONTO')]")))
    button.click()

                
finally:
    time.sleep(3)
    ctypes.windll.user32.LockWorkStation()
    driver.quit()
    
