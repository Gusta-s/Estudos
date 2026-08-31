from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
actions = ActionChains(driver)
driver.get("https://carreiras.agibank.com.br/vagas")
assert "Vagas - Agibank Carreiras" in driver.title

# Filtre para a cidade de Campinas.

#Div localizar
menu_localizar = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[2]/div/button")
menu_localizar.click()
#Submenu "buscar..." para localizar cidade
subMenu_Cidade = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[2]/div/div/div[1]/input")
subMenu_Cidade.send_keys("Campinas")
#Posição da cidade de Campinas
cidade = driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div/aside/div/div[2]/div/div/div[2]/div/div/button")
actions.move_to_element(cidade).click().perform()


# Filtre o departamento 
menu_departamento = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[3]/div/button")
menu_departamento.click()
#SubMenu "Buscar..." para localizar selecionar "Tecnologia"
subMenu_departamento = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[3]/div/div/div[1]/input")
subMenu_departamento.send_keys("Tecnologia")
#posição tecnologia
tecnologia = driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div/aside/div/div[3]/div/div/div[2]/div/button")
actions.move_to_element(tecnologia).click().perform()