from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1 - Acessando o site
browser = webdriver.Firefox()

browser.get('https://registro.br')

# 2 - Buscando elementos
elem = browser.find_element(By.ID, 'is-avail-field')
elem.clear()
elem.send_keys('botscompythoon.com.br')
elem.send_keys(Keys.ENTER)
time.sleep(10)
# browser.save_screenshot('dominio.png')

# 3 - Buscando informações
results = browser.find_elements(By.TAG_NAME, 'strong')

print(f'Domínio {results[1].text} está {results[2].text}')
# import pdb
# pdb.set_trace()
# browser.quit()