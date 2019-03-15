from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

import xlrd

import  time


wb1=webdriver.Chrome()

wb = xlrd.open_workbook("/Users/amit.saxena/PycharmProjects/Amit/Resources/data (1).xlsx")
worksheet = wb.sheet_by_index(1)

for i in range(0,3):

    for j in range(0,3):

        s = worksheet.cell(i,j).value

        print(s)

       # wb1 = webdriver.Safari()

        wb1.get(s)

        wb1.maximize_window()

        sgn = WebDriverWait(wb1, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#text"))).click()

        time.sleep(2)

        if wb1.find_element_by_xpath("//content[text()='Sign in']").is_displayed():

            wb1.find_element_by_xpath("//input[@aria-label='Email or phone']").send_keys("view-support@youplus.com")
            time.sleep(3)
            wb1.find_element_by_xpath("//span[text()='Next']").click()
            time.sleep(3)

            a=wb1.find_element_by_xpath("//div[text()='Enter your password']").is_enabled()

            print("done")

            time.sleep(20)

            n=WebDriverWait(wb1,120).until(EC.presence_of_element_located((By.XPATH,"//*[@id='passwordNext']//span")))
            n.click()

            time.sleep(2)
            wb1.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("viewsupport")
            time.sleep(2)
            wb1.find_element_by_xpath("//span[text()='Next']").click()

            time.sleep(4)

            wb1.execute_script("window.scrollTo(0, 500)")

            print ("done")

            time.sleep(10)

            wb1.find_element_by_css_selector("#simplebox-placeholder").click()

            time.sleep(2)
            wb1.find_element_by_xpath("//*[@id='contenteditable-textarea']").send_keys("HIIIIIIIII")

            wb1.save_screenshot("/Users/amit.saxena/PycharmProjects/Amit/Results/image.png")

            time.sleep(3)
            # wb1.find_element_by_xpath("//*[@id='contenteditable-textarea']").click()

            wb1.find_element_by_xpath("//button//img[@id='img']").click()

            time.sleep(5)

            wb1.find_element_by_xpath("//yt-formatted-string[@id='label' and text()='Sign out']").click()

            wb1.quit()

        elif wb1.find_element_by_xpath("//content[text()='Hi View']").is_displayed():

            wb1.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("viewsupport")
            time.sleep(2)
            wb1.find_element_by_xpath("//span[text()='Next']").click()

            time.sleep(3)

            wb1.find_element_by_xpath("//button//img[@id='img']").click()

            wb1.find_element_by_xpath("//yt-formatted-string[@id='label' and text()='Sign out']").click()

            wb1.quit()
        else:

            print("Script has been succesfully completed ")



wb1.quit()
