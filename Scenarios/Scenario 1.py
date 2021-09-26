from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

#Set up driver. Comment/uncomment lines accordingly to test with required browser
#driver = webdriver.Edge(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\msedgedriver.exe")
#driver = webdriver.Chrome(executable_path=r"")
driver = webdriver.Firefox(executable_path=r"C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe")
#driver = webdriver.Opera(executable_path=r"")
#driver = webdriver.Safari(executable_path=r"")

#Acess website to test
driver.get("https://www.fnac.pt/") 
driver.implicitly_wait(5)
driver.find_element_by_id("onetrust-accept-btn-handler").click() #Remove cookie consent so it doesn't obstruct buttons


#STEP 1- Search for George
search_bar = driver.find_element_by_id("Fnac_Search")
search_bar.send_keys("George", Keys.RETURN)
pageNum = 2

'''
#STEP 1 - Verification for correct search
time.sleep(10)
actualSearch = driver.find_element_by_xpath("//div[@class='toolbar-right']//div[@class='Search-title']//span[@class='js-Search-title'][contains(text(),'George')]")
expectedSearch = "George"
assert expectedSearch == actualSearch, f'Error: Expected search for {expectedSearch}, but instead searched for {actualSearch} '
'''

#STEP 2 - Verify if 'Fascism and Democracy' is displayed in results
#Iterate through search results pages
while True:
    try:
        driver.find_element_by_xpath("//a[contains(@class,'Article-title js-minifa-title js-Search-hashLink')][contains(text(),'Fascism and Democracy')]")
        print("TEST PASSED - Book found in search results")
        break

    except NoSuchElementException:    
        print("Searching next page...")
        driver.get(f"https://www.fnac.pt/SearchResult/ResultList.aspx?ItemPerPage=20&PageIndex={pageNum}&Search=George&sft=1")
        pageNum += 1
        continue

    except:    
        print("TEST FAILED - Book not found")
        driver.quit()
        break


#STEP 3 - Make sure book's description contains the word 'word'
bookDescription = driver.find_element_by_xpath("/html/body/div[3]/div/div[6]/div/div[9]/article[1]/form/div[2]/div/div[1]/p/span").text
if 'world' in bookDescription:
    print("TEST PASSED - 'word' is present in book's description")
else:
    print("'word' isn't present in book's description")

#Shutdown
print("Scenario 1 - Finished test")
driver.close()