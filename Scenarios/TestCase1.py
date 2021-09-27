from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class Test1(unittest.TestCase):
    
    def setUpClass():
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(5)

    #Pesquisar por 'George'
    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons
        search_bar = driver.find_element_by_id("Fnac_Search")
        search_bar.send_keys("George", Keys.RETURN)
        search_result = driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div[1]/div/span[1]").text
        assert search_result == 'George'

    #Validar que o livro 'Fascism and Democracy' se encontra listado nos resultados
    def test2(self):
        pageNum = 2
        while True:
            try:
                expectedBook = driver.find_element_by_xpath("//a[contains(@class,'Article-title js-minifa-title js-Search-hashLink')][contains(text(),'Fascism and Democracy')]")
                assert expectedBook
                break
            except NoSuchElementException:    
                driver.get(f"https://www.fnac.pt/SearchResult/ResultList.aspx?ItemPerPage=20&PageIndex={pageNum}&Search=George&sft=1")
                pageNum += 1
                continue
            except:    
                break

    #Validar que a descrição do livro contém a palavra 'world'
    def test3(self):
        bookDescription = driver.find_element_by_xpath("/html/body/div[3]/div/div[6]/div/div[19]/article[1]/form/div[2]/div/div[1]/p/span").text
        assert 'world' in bookDescription

    def tearDownClass():
        driver.close()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
