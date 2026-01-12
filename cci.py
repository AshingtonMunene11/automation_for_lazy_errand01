from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Setup Chrome driver ---
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")       # run without GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# --- Open the form ---
form_url = "https://forms.office.com/pages/responsepage.aspx?id=Dzfy7eMY60ib7EQaQFgQmOJDM5ntp75Cmr0KCY05-uJUMUUwOUcyVFMwSlZUTUlHNTg3S1VUVEhHNy4u"
driver.get(form_url)

wait = WebDriverWait(driver, 15)

# --- Fill Question 1: Date ---
date_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Date picker"]')))
date_field.send_keys("01/12/2026")

# --- Fill Question 2: Application Site (radio button) ---
site_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"CareerBox Tatu City")]')))
site_option.click()

# --- Fill text fields (Questions 3–10) ---
all_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@placeholder="Enter your answer"]')))

all_inputs[0].send_keys("Cyril Kaari")          # Employee’s Name
all_inputs[1].send_keys("CCIK18375")            # Employee’s Code
all_inputs[2].send_keys("Shutterfly")           # Employee’s Campaign
all_inputs[3].send_keys("Ashington Munene")     # Referral’s Full Name
all_inputs[4].send_keys("37752085")             # Referral’s ID Number
all_inputs[5].send_keys("0788552022")           # Referral’s Phone Number
all_inputs[6].send_keys("Contact Center Agent") # Position Interested In
all_inputs[7].send_keys("Referral")             # How did you hear about us?

# --- Fill Question 11: Campaign (radio button) ---
campaign_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"International")]')))
campaign_option.click()

# --- Submit the form ---
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-automation-id="submitButton"]')))
submit_button.click()

time.sleep(5)  # wait for confirmation page

print("Form submitted successfully!")

driver.quit()

