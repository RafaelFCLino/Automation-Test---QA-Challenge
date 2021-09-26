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

#STEP 1- Reach 1984 book page
search_bar = driver.find_element_by_id("Fnac_Search")
search_bar.send_keys("1984")
driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[1]/div/div[1]/ul/li[1]/a").click()

#STEP 2 - Consult author's biography
#Reach comment page
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[1]/a").click()


#STEP 3 - Validate that 'Animal Farm' is part of his work
try:
    driver.find_element_by_partial_link_text("Animal-Farm")
    print("TEST PASSED - Animal Farm present in George Orwell's Bio")
except:
    print("TEST FAILED - Animal Farm not present in George Orwell's Bio")
    pass

#Shutdown
print("Scenario 4 - Finished test")
driver.close()