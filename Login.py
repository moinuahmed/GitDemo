from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

login_username = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input"
driver.find_element_by_xpath(login_username).send_keys("Admin")

time.sleep(2)

login_pass = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input"
elm = driver.find_element_by_xpath(login_pass)
elm.send_keys("admin123")

time.sleep(2)

elm.submit()

# (Note : Entering correct username and password showing invalid credentials)






