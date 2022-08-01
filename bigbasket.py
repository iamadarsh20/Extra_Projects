from lib2to3.pgen2 import driver
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains



chrome_path = r"D:\BACKUP\C\Downloads\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

driver.maximize_window()
driver.get("https://www.bigbasket.com/?utm_source=google&utm_medium=cpc&utm_campaign=Brand-MUM&gclid=EAIaIQobChMI5czW1Z-x-AIVD7aWCh2EuQVxEAAYASAAEgIru_D_BwE")
action = ActionChains(driver)

# firstaction = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/a')
firstaction = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/a')))

action.click(firstaction).perform()


# secondaction = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/ul/li/mega-nav-template/div/ul/li[5]/a')
secondaction = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/nav/div/div/ul/li[1]/ul/li/mega-nav-template/div/ul/li[5]/a')))
action.click(secondaction).perform()