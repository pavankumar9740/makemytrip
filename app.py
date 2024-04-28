import os
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.makemytrip.com/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
driver.implicitly_wait(10)
driver.find_element(By.ID,'fromCity').click()
from_state=driver.find_element(By.XPATH,"//input[@placeholder='From']")
from_state.send_keys('BLR')
driver.find_element(By.XPATH,"//*[@class='makeFlex column flexOne']").click()
driver.implicitly_wait(2)
# driver.find_element(By.XPATH,"//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
# driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']//div[@class='makeFlex flexOne column']").click()
# driver.find_element(By.XPATH,"//body/div[@id='root']/div[@id='top-banner']/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]").click()
# driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']//div[@class='mak
driver.find_element(By.ID,'toCity').click()
to_state=driver.find_element(By.XPATH,"//input[@placeholder='To']")
to_state.send_keys('ZER')
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//div[@aria-label='Wed May 01 2024']").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Search')]").click()
screenshot_path = os.path.join(os.getcwd(), 'screenshot.png')
driver.save_screenshot(screenshot_path)
driver.implicitly_wait(2)
driver.close()
