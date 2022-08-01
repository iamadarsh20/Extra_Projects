import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
path  = r"C:\Users\kshat\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=4391435195055616227&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062241&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=CjwKCAjwkYGVBhArEiwA4sZLuOVBjRrDU0cMxNAqCqV3S--VvppztQJSXh6OA8TGPsUc7QPJBoRVXBoCk5sQAvD_BwE')
driver.maximize_window()
time.sleep(2)


search = driver.find_element_by_xpath(r'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('helmet for mens bike')
search.send_keys(Keys.RETURN)


view_desc=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div/div[3]/div[1]/h2/a/span')
view_desc.click()

# print(driver.current_window_handle)  # CDwindow-C7E10AAC989B3E0AE3C7CE9D8955C76C - parent

handles = driver.window_handles # return all the values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    # print(driver.title)
    if driver.title == 'helmet for mens bike':
        driver.close

    

about = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[6]/div[4]/div[4]/div[1]/div/h1/span'))).text
time.sleep(5)
print(about)

prod_desc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/div[6]/div[4]/div[4]/div[40]'))).text
time.sleep(5)
print(prod_desc)



