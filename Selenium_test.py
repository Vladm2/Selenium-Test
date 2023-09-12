from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
# from selenium.webdriver.support.ui import WebDriverWait

myOptions = ChromeOptions()
myOptions.add_argument("start-maximized")
driver = webdriver.Chrome(options = myOptions)
# driver.implicitly_wait(50)

# Opens Google
driver.get("https://www.google.com")

# Sekects "Reject cookies"
driver.find_element(By.ID, "W0wltc").click()

# Writes "Facebook" in the searchbar
driver.find_element(By.ID, "APjFqb").send_keys("Facebook")

# Click search button
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]").click()

# Selects first result
driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/a/h3').click()

# Reject optional cookies
driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[1]').click()

# Enters login email
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys("fictional_email@fictional.com")

# Enters login password
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys("Fictional123")

# Clicks "Connect" button
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

assert driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]/text()').text == 'Adresa de e-mail introdusă nu este asociată unui cont. '

time.sleep(500)