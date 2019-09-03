from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

pesquisaPor = "www.google.com" #siga o exemplo: www.google.com
driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
driver.get('https://www.google.com/search?q=related%3A'+str(pesquisaPor)+'') #ABRE A PAGINA DE PESQUISA
time.sleep(3)
j=3
file = open('C:\\DIRETORIO\\ARQUIVO.txt','a')
file.write('\n')
file.write('Sites semelhantes a: '+pesquisaPor)
file.write('\n')
file.write('\n')
proximapagina = 0
while proximapagina != '1':
    for i in range(1,11):
        try:
            driver.find_element_by_xpath('//*[@id="rso"]/div/div/div['+str(i)+']/div/div/div[1]/a/div/cite') #seleciona o primeiro resultado da pesquisa
        except NoSuchElementException:
            site = 1
            pass
        else:
            site = driver.find_element_by_xpath('//*[@id="rso"]/div/div/div['+str(i)+']/div/div/div[1]/a/div/cite') #seleciona o primeiro resultado da pesquisa
        if site == 1:
            print("vazio")
        else:
            print(site.text)
            file = open('C:\\Users\\Neemias\\Desktop\\python testes\\sites-para-visitar.txt','a')
            file.write(site.text)
            file.write('\n')
    try:
         proximapagina = driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr/td['+str(j)+']/a') #encontra o link para a proxima pagina
    except NoSuchElementException:
        proximapagina = 1 #se não encontrar a proxima pagina, grave o valor 1 para a variavel
        pass
    else:
        proximapagina.click() # se encontrar, clique para a proxima pagina
        time.sleep(8)
        j += 1
    if proximapagina == 1: # se o valor da variavel for igual a 1, impima a seguinte frase
        print("não tem mais paginas")
        break
