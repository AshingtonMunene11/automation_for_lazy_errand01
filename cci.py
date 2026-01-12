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

# --- Collect all text inputs (Questions 3–8) ---
all_inputs = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//input[@placeholder="Enter your answer"]')))
print("Found", len(all_inputs), "text input fields")

answers = [
    "Cyril Kaari",          # Employee’s Name
    "CCIK18375",            # Employee’s Code
    "Shutterfly",           # Employee’s Campaign
    "Ashington Munene",     # Referral’s Full Name
    "37752085",             # Referral’s ID Number
    "0788552022"            # Referral’s Phone Number
]

for i, value in enumerate(answers):
    if i < len(all_inputs):
        all_inputs[i].send_keys(value)
    else:
        print(f"Skipping answer {i} ({value}) — no matching input field")

# --- Fill Question 9: Position Interested In (radio button) ---
position_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Contact Center Agent")]')))
position_option.click()

# --- Fill Question 10: How did you hear about us? (radio button) ---
referral_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Referral")]')))
referral_option.click()

# --- Fill Question 11: Campaign (radio button) ---
campaign_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"International")]')))
campaign_option.click()

# --- Submit the form ---
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-automation-id="submitButton"]')))
submit_button.click()

# --- After submit ---
time.sleep(5)
body_text = driver.find_element(By.TAG_NAME, "body").text

if "Your response was recorded" in body_text or "Thank you" in body_text:
    print("Submission confirmed!")
elif "Required" in body_text:
    print("Submission failed — required fields missing.")
else:
    print("Submission may not have been accepted. Page text:", body_text[:200])

driver.quit()
