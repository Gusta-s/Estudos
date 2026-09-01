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
submenu_estado = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[3]/div[2]/form[2]/div[4]/div")
submenu_estado.send_keys("São Paulo (SP)")
submenu_estado.send_keys(Keys.TAB)

#Filtre por Cidade
cidade = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[3]/div[2]/form[2]/div[5]/div")
cidade.click()
cidade.send_keys("Campinas")
cidade.send_keys(Keys.TAB)

#Filtre o tipo de vaga 
tipo_vaga = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section[3]/div[2]/form[2]/div[2]/div/div/div[1]/div[2]")
tipo_vaga.click()
tipo_vaga.send_keys("Estágio")
tipo_vaga.send_keys(Keys.TAB)