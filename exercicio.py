from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

driver.get("https://preproducao-esig.ufca.edu.br/sigaa/public/home.jsf")

sleep (2)

#cria um loop para verificar se o usuario esta logado pela url

while driver.current_url != "https://preproducao-esig.ufca.edu.br/sigaa/graduacao/geral.jsf":
    sleep(2)
    print("Aguardando login")
    sleep(2)
    # enquanto for diferente do link da pagina de graduação

driver.find_element(By.LINK_TEXT, "Atualizar Dados Pessoais" ).click()

sleep(2)

driver.find_element(By.ID, "formulario:matriculaDiscente" ).click()

sleep(2)

# Digita a matricula pelo terminal  
matricula = getpass("Digite a matricula: ")
# clica em continuar
driver.find_element(By.ID, "formulario:matriculaDiscente" ).send_keys(matricula)
#clica em buscar
driver.find_element(By.ID, "formulario:buscar" ).click()
#seleciona o discente
driver.find_element(By.ID, "form:selecionarDiscente" ).click()
