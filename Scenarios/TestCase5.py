from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class Test5(unittest.TestCase):
    
    def setUpClass():
        #Set up driver. Comment/uncomment lines accordingly to test with required browser
        global driver
        driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
        driver.implicitly_wait(10)

    def test1(self):
        driver.get("https://www.fnac.pt/") 
        driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons
        search_bar = driver.find_element_by_id("Fnac_Search")
        search_bar.send_keys("Fascism and Democracy", Keys.RETURN)
        searchResult = driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div[1]/div/span[1]").text
        assert searchResult == 'Fascism and Democracy'

    def test2(self):
        driver.find_element_by_xpath("/html/body/div[3]/div/div[6]/div/div[1]/article[1]/form/div[3]/div/div/div/button").click()
        ItemAdded = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div")
        assert ItemAdded

    def test3(self):
        driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
        try: 
            driver.find_element_by_id("onetrust-accept-btn-handler").click() #remove temporary ad
        except:
            pass
        numItemsInCart = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[1]/div[1]/div/h2/span/span").text
        assert numItemsInCart == "1 PRODUTO"
 
    def test4(self):
        itemPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[1]/span[2]/span").text
        item = float(itemPrice.replace('€','.'))

        deliveryPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[2]/span[2]/span").text
        delivery = float(deliveryPrice.replace('€','.'))

        totalPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[3]/span[2]/span").text
        total = float(totalPrice.replace('€','.'))

        expectedTotal = item + delivery
        assert total == expectedTotal

    def tearDownClass():
        driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())