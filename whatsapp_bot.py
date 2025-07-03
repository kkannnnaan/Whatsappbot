from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start Chrome and open WhatsApp Web
# If chromedriver is not in PATH, specify the path: webdriver.Chrome(executable_path='path/to/chromedriver')
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
input("Scan the QR code in the browser, then press Enter here...")

# Find a chat by contact name
contact = "Friend Name"  # Change this to the name as it appears in WhatsApp
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(contact)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Send the initial bot message
msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
msg_box.send_keys("Hi, How can I help you today?" + Keys.ENTER) 