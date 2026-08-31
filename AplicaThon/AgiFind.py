from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
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
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",cidade)
cidade.click()


# Filtre o departamento 
menu_departamento = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[3]/div/button")
menu_departamento.click()
#SubMenu "Buscar..." para localizar selecionar "Tecnologia"
subMenu_departamento = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[3]/div/div/div[1]/input")
subMenu_departamento.send_keys("Tecnologia")
#posição tecnologia
tecnologia = driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div/aside/div/div[3]/div/div/div[2]/div/button")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",tecnologia)
tecnologia.click()

# Pesquise por "Estágio"
menu_oportunidade = driver.find_element(By.XPATH, "/html/body/main/section[2]/div/div/aside/div/div[1]/div/input")
menu_oportunidade.click()
menu_oportunidade.send_keys("Estágio")
vaga_result = driver.find_element(By.XPATH,"/html/body/main/section[2]/div/div/div/div/div[2]/div[1]/p[1]")
sem_vaga = vaga_result.text
if sem_vaga == "Nenhuma vaga aberta encontrada com os filtros selecionados.":
    print("=====================================================\n Infelizmente não foi encontrado vagas para estágio 😞\n=====================================================")
else:
    print("=============================================\n UMA OPORTUNIDADE FOI ENCONTRADA CORRE !!!! 😃\n=============================================")