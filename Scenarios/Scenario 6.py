from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

#STEP 1- Search for store 'Lisboa'
driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/div[2]/div[1]/a").click()
search_bar = driver.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/form/fieldset/input")
search_bar.send_keys("Lisboa", Keys.RETURN)

#STEP 2 - Select store 'Almada'
try:
    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/ul[2]/li[5]/div/div[2]/span[1]/a").click()
except:
    print("TEST FAILED - No store named 'Almada' in store search results")

#STEP 3 - Validate that postal code for Almada store is '2810-354'
adress = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[1]/div[1]/p[2]").text


#STEP 4 - Validate that store is open everyday from 10:00 to 23:00
monday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[1]/span[2]").text
tuesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[2]/span[2]").text
wednesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[3]/span[2]").text
thursday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[4]/span[2]").text
friday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[5]/span[2]").text
saturday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[6]/span[2]").text
sunday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[7]/span[2]").text

if monday == tuesday == wednesday == thursday == friday == saturday == sunday == "10:00 - 23:00":
    print("TEST PASSED - Store is open everyday from 10:00 to 23:00")
else:
    print("TEST FAILED - Store isn't open everyday from 10:00 to 23:00")

#Shutdown
print("Scenario 6 - Finished test")
driver.close()