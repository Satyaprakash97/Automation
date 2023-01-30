# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFind_Element_By_Id():
    def locate_by_id_demo(self, login=None):
        #driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        searchbox=driver.find_element(By.CLASS_NAME , 'yt-sme-mobile-input.required_field.email-login-box')
        searchbox.send_keys('satya@gmail.com')
        time.sleep(5)
        cont=driver.find_element(By.ID , 'login-continue-btn')
        cont.click()
        time.sleep(10)
findbyid=DemoFind_Element_By_Id()
findbyid.locate_by_id_demo()