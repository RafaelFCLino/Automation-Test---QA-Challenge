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

#STEP 1- Search for 'Fascism and Democracy'
search_bar = driver.find_element_by_id("Fnac_Search")
search_bar.send_keys("Fascism and Democracy", Keys.RETURN)

#STEP 2 - Add book to shopping cart
driver.find_element_by_xpath("/html/body/div[3]/div/div[6]/div/div[1]/article[1]/form/div[3]/div/div/div/button").click()

#STEP 3 - Validate that number of cart items is 1
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[1]/a").click()
numItemsInCart = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[1]/div[1]/div/h2/span/span").text
if numItemsInCart == "1 produto":
    print("TEST PASSED - Cart shows 1 item")
else:
    print("TEST FAILED - Cart doesn't show 1 item")

#STEP 4 - Validate that total (VAT incl) equals item price plus estimated delivery costs
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/div[1]/a").click()

itemPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[1]/span[2]/span").text
item = float(itemPrice.replace('€','.'))

deliveryPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[2]/span[2]/span").text
delivery = float(deliveryPrice.replace('€','.'))

totalPrice = driver.find_element_by_xpath("/html/body/div[1]/div/section/div/div/div[2]/section/div[3]/div[3]/span[2]/span").text
total = float(totalPrice.replace('€','.'))

expectedTotal = item + delivery

if total == expectedTotal:
    print("ok")
else:
    print("Nok")

#Shutdown
print("Scenario 5 - Finished test")
driver.close()