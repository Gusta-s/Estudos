from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://institutoeldorado.gupy.io/")
assert "Vagas Instituto de Pesquisas Eldorado" in driver.title

# Filtre por estado
estado = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[3]/div[2]/form[2]/div[4]/div/div/div[1]/div[2]")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",estado)
estado.click()
submenu_estado = driver.find_element(By.CSS_SELECTOR, "#state-select")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",submenu_estado)
submenu_estado.click()
submenu_estado.send_keys("São Paulo")
submenu_estado.send_keys(Keys.TAB)

#Filtre por Cidade
cidade = driver.find_element(By.CSS_SELECTOR, "#city-select")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",cidade)
cidade.click()
cidade.send_keys("Campinas")
cidade.send_keys(Keys.TAB)

#Filtre o tipo de vaga 
tipo_vaga = driver.find_element(By.CSS_SELECTOR, "#job-type-select")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",tipo_vaga)
tipo_vaga.click()
tipo_vaga.send_keys("Estágio")
tipo_vaga.send_keys(Keys.TAB)

#Selecione área da vaga 
area = driver.find_element(By.CSS_SELECTOR, "#department-select")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",area)
area.click()
area.send_keys("Software")
area.send_keys(Keys.TAB)