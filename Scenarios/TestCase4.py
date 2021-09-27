from selenium import webdriver
import unittest
import HtmlTestRunner

class Test4(unittest.TestCase):
    
    def setUpClass():
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(5)

    #Pesquisar pelo livro '1984'
    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons
        search_bar = driver.find_element_by_id("Fnac_Search")
        search_bar.send_keys("1984")
        driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/ul/li[1]/a").click()
        bookPage = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/h1").text
        assert bookPage == '1984'

    #Consultar biografia do autor
    def test2(self):
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[1]/a").click()
        authorPage = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/span").text
        assert authorPage == 'George Orwell'

    #Validar que o livro 'Animal Farm' faz parte das obras de sua autoria
    def test3(self):
        animalFarmPresent = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/section[1]/div[2]/div/div/div[7]/article/form/div[3]/span/a")
        assert animalFarmPresent

    def tearDownClass():
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())