from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:\\Users\\LabInfo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.netshoes.com.br/auth/login")
    driver.implicitly_wait(2) 
    print ('0')
    email_login = driver.find_element(By.XPATH, '//*[@id="user"]')
    email_login.send_keys("hanna.luzzi@hotmail.com")
    print ('1')

    senha_login = driver.find_element(By.XPATH, '//*[@id="password"]')
    senha_login.send_keys("182436")
    print ('2')

    email_login.send_keys(Keys.ENTER)
    print ('4')

    barra_pesquisa = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-input"))

        )
    
    barra_pesquisa =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search-input"]')))
    barra_pesquisa.send_keys("Tênis")
    barra_pesquisa.send_keys(Keys.ENTER)
    print("Teste Passou! Comentário postado.")
except:
    print("Teste Falhou! Não foi possível postar o comentário.")

driver.quit()