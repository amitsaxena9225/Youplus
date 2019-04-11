from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import xlrd
import xlwt
import time
DB_USER ='youplus'
DB_PASS= 'youplus9091'

client = MongoClient('ind.dev.mdb-mongos01.yupl.us', 27017)
db = client.DEV_Shard_DB

if db.authenticate(DB_USER, DB_PASS, source='youplus_development'):
   print("authenticated, do ...")

else:
   print("not authenticated, not connected, do something else")
   
   
mydb =client["youplus_development"]
mycol = mydb["youplus_q_tags"]

#for x in mycol.find_one({}):

#for x in mycol.find({'email':"santoshkumar@youplus.co"}):

#for x in mycol.watch():# print(x)

#myquery = { "source_link": {"$gt": "^h"} }
myresult = mycol.find({},{"_id": 0,"source_link": 1,"is_analyzed":1,"is_auto_processed":1}).limit(100)

a=[]
for x in myresult:
#for x in mycol.find(myquery):
  #print(x)
  
  if 'source_link' in x.keys() and 'is_analyzed'in x.keys() and 'is_auto_processed' in x.keys():
      print(x['is_analyzed'],x['is_auto_processed'],x['source_link'])
      #a=[]
      if x['is_analyzed']==False and x['is_auto_processed']==False:
          #print("loop in second if condition")
          a.append(x['source_link'])
          #print(a)
#print(a)

while("" in a) : 
    a.remove("")

print(a)
print(len(a))

final_list = []
for num in a: 
    if num not in final_list: 
        final_list.append(num)


print(final_list)
print(len(final_list))

#wb = xlrd.open_workbook(r'C:\Users\Administrator\Desktop\exce.xlsx')
#worksheet = wb.sheet_by_index(0)

for i in range(1,3):

    for j in range(0,3):

        #s = worksheet.cell(i,j).value

        #print(s)
        
        wb1=webdriver.Chrome()

        time.sleep(5)

        abc=wb1.get(final_list[i])
        print(abc)

        wb1.maximize_window()

        sgn = WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Sign in']"))).click()

        time.sleep(2)

        if  WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Email or phone']"))).is_displayed():
            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//input[@aria-label='Email or phone']"))).send_keys("view-support@youplus.com")
            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//span[text()='Next']"))).click()

            #a=wb1.find_element_by_xpath("//div[text()='Enter your password']").is_enabled()

            print("done")

            time.sleep(6)

            n=WebDriverWait(wb1,120).until(EC.presence_of_element_located((By.XPATH,"//*[@id='passwordNext']//span")))
            n.click()
            print("clicked on Next button")

            time.sleep(2)
            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input"))).send_keys("viewsupport")
            time.sleep(2)
            print("entered the password")
            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//span[text()='Next']"))).click()

            time.sleep(4)
            print("clicked on Next button")

            wb1.execute_script("window.scrollTo(0, 500)")

            time.sleep(4)
            print("Scrolled first time")

            wb1.execute_script("window.scrollTo(0, 500)")

            time.sleep(10)
            print("Scrolled second time")

            

            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#simplebox-placeholder"))).click()
            print("found etxt area")

            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//*[@id='contenteditable-textarea']"))).send_keys("HIIIIIIIII")

            print("enetered HIIIII")
            st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
            file_name = "youplus" + st + ".png"

            wb1.save_screenshot(r"C:\Users\Administrator\Desktop"+file_name)

            # wb1.find_element_by_xpath("//*[@id='contenteditable-textarea']").click()

            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//button//img[@id='img']"))).click()

            #time.sleep(5)

            WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.XPATH,"//yt-formatted-string[@id='label' and text()='Sign out']"))).click()
            print("cycle is completed")
           # time.sleep(3)
            wb1.quit()
      
#update the db status
myquery = { "is_comented": "false" }
newvalues = { "$set": { "is_comented": "true" } }

mycol.update_one(myquery, newvalues)

#

myquery_1 = { "is_comented_status": "in_queue" }
newvalues_1 = { "$set": { "is_comented_status": "done" } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

	
