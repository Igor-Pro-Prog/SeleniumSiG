from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json

with open("exercicio.json", "r") as arquivo:
    pei=json.load(arquivo)

driver = webdriver.Firefox()


driver.get(pei["SiteUFRN"])

usuario="123"
senha="123"

user = driver.find_element(By.NAME, pei["inputNome"])
user.send_keys(usuario)

senha = driver.find_element(By.NAME, pei["inputSenha"])
senha.send_keys(senha)

botao = driver.find_element(By.XPATH, pei["xpathBotaoEntrar"])
botao.click()