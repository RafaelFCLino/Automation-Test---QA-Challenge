# Automation-Test---QA-Challenge

## Como utilizar

### 1) Instalar as ferramentas

python 3.9 -> https://www.python.org/downloads/
selenium -> na linha de comandos correr 'pip install selenium'
HTMLTestRunner -> na linha de comandos correr 'pip install htmltestrunner-rv'


### 2) Instalar o browser
Os scripts estão preparados para ser corridos em Mozilla Firefox, pelo que o browser deverá ser instalado antes (https://www.mozilla.org/pt-PT/firefox/new/).
Após instalação, é necessário configurar o caminho para o executável do webdriver nos scripts. Para isto, em .\Automation-Test---QA-Challenge\Scenarios abrir os ficheiros TestCase[1-6], aceder à linha 'driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")' presente em setUpClass de cada script e corrigir o executable_path para o atual diretório do driver.

É possível alterar o browser para outro suportado por selenium, seguindo as indicações presentes na área 'Platforms Supported by Selenium' em https://www.selenium.dev/downloads/

### 3) Correr os testes
Para executar cada teste individual é necessário correr o script ao TestCase correspondente em qualquer interpretador de python ou, através da linha de comandos, acedendo ao diretório ...Automation Test - QA Challenge\Scripts e executando [NomeDoScript].py
Para executar toda a bateria de testes deve ser corrido o script FnacTest.py

### 4) TestLogs
A execução de cada teste irá gerar na pasta reports um ficheiro html onde consta o resultado da execução.
