from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\Rafael Lino\Desktop\Automation Test - QA Challenge\geckodriver.exe')


driver.get("https://www.fnac.pt/Fnac-Almada/Fnac-Almada/cl7/w-4") 
time.sleep(10)
driver.implicitly_wait(5)

monday = driver.find_element_by_xpath(f"/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[{i}]/span[2]").text
tuesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[2]/span[2]").text
wednesday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[3]/span[2]").text
thursday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[4]/span[2]").text
friday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[5]/span[2]").text
saturday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[6]/span[2]").text
sunday = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[4]/div[1]/div/div/section[2]/div[1]/div/p[7]/span[2]").text

driver.find_elements_by_xpath("")



#lastCommentDate = driver.find_elements_by_xpath(f"/html/body/div[2]/section/div/div/div/section{lastComment}/div/div/div[2]").text
#print(lastCommentDate)
#driver.quit()

