from selenium import webdriver
import unittest
import HtmlTestRunner

class Test3(unittest.TestCase):
    
    def setUpClass():
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(5)

    #Pesquisar pelo livro '1984'
    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.implicitly_wait(5)
        driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons
        search_bar = driver.find_element_by_id("Fnac_Search")
        search_bar.send_keys("1984")
        driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/ul/li[1]/a").click()
        bookPage = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/h1").text
        assert bookPage == '1984'

    #Validar que o comentário mais antigo publicado sobre o livro é de 22/08/2018
    def test2(self):
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[2]/div[1]/a/span/span[2]").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[5]/div/header/div/a").click()
        #Reach the last page in comments to access oldest comment. If its already the last page get the comment date from the last comment
        try:
            driver.find_element_by_xpath("/html/body/div[2]/section/div/div/div/section[11]/ul/li[4]/button").click()
        except:
            pass
        comments = driver.find_elements_by_class_name("f-reviews-date")
        length = len(comments)
        lastCommentDate = driver.find_element_by_xpath(f"/html/body/div[2]/section/div/div/div/section[{length}]/div/div/div[2]/p").text
        assert lastCommentDate == 'Publicada a 22 ago 2018'

    #Validar que existem 0 classificações com '1 estrela'
    def test3(self):
        zeroStarScore = driver.find_element_by_xpath("/html/body/div[2]/section/div/div/section[1]/header/div[3]/div/div/ul/li[1]/div[1]/div/span").text
        assert zeroStarScore == '0'

    def tearDownClass():
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())