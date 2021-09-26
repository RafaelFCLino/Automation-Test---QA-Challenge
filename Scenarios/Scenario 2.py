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

#STEP 1- Search for 1984
search_bar = driver.find_element_by_id("Fnac_Search")
search_bar.send_keys("1984")
driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/ul/li[1]/a").click()

'''
#STEP 1 - Verification for correct search
time.sleep(10)
actualSearch = driver.find_element_by_xpath("//div[@class='toolbar-right']//div[@class='Search-title']//span[@class='js-Search-title'][contains(text(),'George')]")
expectedSearch = "George"
assert expectedSearch == actualSearch, f'Error: Expected search for {expectedSearch}, but instead searched for {actualSearch} '
'''

#STEP 2 - Verify if author is George Orwell
author = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[1]/a").text
if 'George Orwell'in author:
    print("TEST PASSED - Author is George Orwell")
else:
    print("TEST FAILED - Author isn't George Orwell")

#STEP 3 - Verify if ISBN is 9789726081890
isbn = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[1]/dl[4]/dd/p").text
if isbn == '9789726081890':
    print("TEST PASSED - ISBN is 9789726081890")
else:
    print("TEST FAILED - ISBN isn't 9789726081890")

#STEP 4 - Verify if number of pages is 314
npages = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[2]/dl[1]/dd/p").text
if npages == '314':
    print("TEST PASSED - Page number is 314")
else:
    print("TEST FAILED - Page number isn't 314")

#STEP 5 - Verify if book dimensions are 13 x 21 cm
bookDimensions = driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[7]/div/div/div[1]/div[1]/dl[5]/dd/p").text
if bookDimensions == '13 x 21 cm':
    print("TEST PASSED - book dimensions are 13 x 21 cm")
else:
    print("TEST FAILED - book dimensions aren't 13 x 21 cm")

#Shutdown
print("Scenario 2 - Finished test")
driver.close()