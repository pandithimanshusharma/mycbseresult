from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pickle

result_file = open('result cbse 12th.txt','a')

stu_marks = {}
driver = webdriver.Chrome('C:/Users/user/PycharmProject/mydjango/misson pisa/chromedriver.exe')
driver.get("https://www.cbseresults.nic.in/class12/Class12th21.htm")
time.sleep(2)
if driver.current_url =='https://www.cbseresults.nic.in/class12/Class12th21.htm':
    driver.find_element_by_xpath('//*[@id="details-button"]').click()
    driver.find_element_by_xpath('//*[@id="proceed-link"]').click()
for i in range(25658116,25658196):
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input').send_keys(i)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input').send_keys(84042)
    driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]').click()
    page_source = driver.page_source
    soup = BeautifulSoup(page_source,'html.parser')
    print(soup) 
