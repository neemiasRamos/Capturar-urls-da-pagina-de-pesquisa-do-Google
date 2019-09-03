# web-scraping-resultado-pesuisa-do-google

# Web Scraping - Capturar urls da pagina de pesquisa do Google

A aplicação acessa o google e faz uma pesuisa por sites relacionados, utilizando a query search?q=related%3A. Dessa forma, os resultados que aparecem são únicos, de modo geral, e isso torna mais simples a captura das urls. 

O princípal objetivo é descobrir novos sites.


## Requisitos para executar a aplicação em seu computador
1. Web Driver do Google Chrome - [ChromeDriver](http://chromedriver.chromium.org/downloads)
2. Python 3.7
3. Bibliotecas

Biblioteca    | Baixar        | pip
------------- | ------------- | ---------
selenium      | [Download](https://pypi.org/project/selenium/)                       | pip install selenium
pyautogui     | [Download](https://pyautogui.readthedocs.io/en/latest/install.html)  | pip install PyAutoGUI
time          | [Documentação](https://docs.python.org/3/library/time.html)          | --

## Instruções
1. Clone o repositório
2. Instale o ChromeDriver
3. Altere o caminho do webdriver no codigo
~~~
    driver = webdriver.Chrome('C:\chrome\chromedriver.exe')
~~~
2. Abra o IDLE
3. Abra o arquivo .py e execute


![stack Overflow](https://github.com/neemiasRamos/web-scraping-resultado-pesuisa-do-google/blob/master/sDWw49Hmij.gif)
