from selenium import webdriver
import unittest
import HtmlTestRunner

class Test2(unittest.TestCase):
    
    def setUpClass():
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(5)

    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.implicitly_wait(5)
        driver.find_element_by_id("onetrust-accept-btn-handler").click()    #Remove cookie consent so it doesn't obstruct buttons
        search_bar = driver.find_element_by_id("Fnac_Search")
        search_bar.send_keys("1984")
        driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/ul/li[1]/a").click()
        bookPage = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/h1").text
        assert bookPage == '1984'

    def test2(self):
        author = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[1]/a").text
        assert author == 'George Orwell (Autor)'

    def test3(self):
        isbn = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[1]/dl[4]/dd/p").text
        assert isbn == '9789726081890'

    def test4(self):
        npages = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[2]/dl[1]/dd/p").text
        assert npages == '314'

    def test5(self):
        bookDimensions = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[1]/dl[5]/dd/p").text
        assert bookDimensions == '13 x 21 cm'

    def tearDownClass():
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
