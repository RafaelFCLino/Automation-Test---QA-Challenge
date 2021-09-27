from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import datetime

class Test6(unittest.TestCase):
    
    def setUpClass():
        #Set up driver. Comment/uncomment lines accordingly to test with required browser
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(5)

    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons
        driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/div[2]/div[1]/a").click()
        search_bar = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/form/fieldset/input")
        search_bar.send_keys("Lisboa", Keys.RETURN)
        searchResult = driver.find_element_by_id('address').get_attribute("value")
        assert searchResult == 'Lisboa'

    def test2(self):
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/ul[2]/li[5]/div/div[2]/span[1]/a").click()
        storeAlmada = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/p").text
        assert storeAlmada == 'Fnac Almada'

    def test3(self):
        adress = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[1]/div[1]/p[2]").text
        assert '2810-354' in adress

    def test4(self):
        weekday = datetime.datetime.today().weekday() 

        if weekday == 0:
            monday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[1]/strong[2]").text
        else:
            monday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[1]/span[2]").text
        
        if weekday == 1:
            tuesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[2]/strong[2]").text
        else:
            tuesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[2]/span[2]").text

        if weekday == 2:
            wednesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[3]/strong[2]").text
        else:
            wednesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[3]/span[2]").text

        if weekday == 3:
            thursday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[4]/strong[2]").text
        else:
            thursday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[4]/span[2]").text

        if weekday == 4:
            friday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[5]/strong[2]").text
        else:
            friday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[5]/span[2]").text

        if weekday == 5:
            saturday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[6]/strong[2]").text
        else:
            saturday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[6]/span[2]").text

        if weekday == 6:
            sunday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[7]/strong[2]").text
        else:
            sunday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[7]/span[2]").text

        assert monday == tuesday == wednesday == thursday == friday == saturday == sunday == "10:00 - 23:00"

    def tearDownClass():
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())