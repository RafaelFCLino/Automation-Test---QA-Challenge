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

#STEP 2 - Verify that oldest published comment is from 22/08/2018
#Reach comment page
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/section[1]/div[2]/div[1]/a/span/span[2]").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div[5]/section[5]/div/header/div/a").click()

'''
The site already has the comments sorted by order but if this changes in the future uncomment this secction
try:
    driver.find_element_by_xpath("/html/body/div[2]/section/div/div/section[2]/div/ul/li[4]/a").click()
except:    
    oldestComment = driver.find_element_by_xpath("/html/body/div[2]/section/div/div/div/section[1]/div/div/div[2]/p").text
'''
#Reach the last page in comments to access oldest comment. If its already the last page get the comment date from the last comment
try:
    driver.find_element_by_xpath("/html/body/div[2]/section/div/div/div/section[11]/ul/li[4]/button").click()
except:
    pass

comments = driver.find_elements_by_class_name("f-reviews-date")
length = len(comments)
lastCommentDate = driver.find_element_by_xpath(f"/html/body/div[2]/section/div/div/div/section[{length}]/div/div/div[2]/p").text

if '22 ago 2018' == lastCommentDate:
    print("TEST PASSED - Oldest comment is from 22/08/2018")
else:
    print("TEST FAILED - Oldest comment isn't from 22/08/2018")

#Shutdown
print("Scenario 3 - Finished test")
driver.close()