from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome() 

username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
search_query = os.getenv("SEARCH_QUERY")
note_message = os.getenv("MESSAGE")

if not username or not password:
    print("Login Credentials are not set.")

driver.get('https://www.linkedin.com/login')

username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
username_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

WebDriverWait(driver, 15).until(EC.url_contains('linkedin.com/feed'))

search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Search']")))

search_input.send_keys(search_query)
search_input.send_keys(Keys.RETURN)
    
all_people_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='See all people results']")))
driver.execute_script("arguments[0].click();", all_people_button)

driver.switch_to.window(driver.window_handles[-1])

WebDriverWait(driver, 10).until(EC.url_contains('search/results/people'))

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.entity-result__title-line")))
profile_button = driver.find_elements(By.CSS_SELECTOR, "span.entity-result__title-line")
span_text = profile_button[0].find_element(By.XPATH, ".//span/a/span/span")
profile_button[0].click()
print(span_text)
WebDriverWait(driver, 10).until(EC.url_contains('linkedin.com/in/'))


for i in range(int(os.getenv("NUMBER_OF_REQUESTS"))):

    driver.execute_script("window.history.go(-1);")

    WebDriverWait(driver, 10).until(EC.url_contains('linkedin.com/search/results/people'))

    profile_buttons = driver.find_elements(By.CSS_SELECTOR, "span.entity-result__title-line a")

    profile_buttons[i].click()

    WebDriverWait(driver, 10).until(EC.url_contains('linkedin.com/in/'))

    time.sleep(3)

    profile_section = driver.find_element(By.CLASS_NAME, "pv-top-card")

    try:

        button = profile_section.find_element(By.XPATH, ".//button[contains(@aria-label, 'Pending')]")
        print(f"{i}: Request already sent! Pending button is present on the profile.")

    except NoSuchElementException:
        
        print(f"{i}: Not Found! -> Pending")
        
        try:

            connect_button = profile_section.find_element(By.XPATH, ".//button[contains(@aria-label, 'Invite')]")
            # driver.execute_script("arguments[0].click();", connect_button[0])
            connect_button.click()
            time.sleep(1)
            note_section = driver.find_element(By.ID, "send-invite-modal")
            print(f"{i}: Clicked Connect Button")
            add_note_button = driver.find_element(By.XPATH, ".//button[contains(@aria-label, 'Add a note')]")
            # driver.execute_script("arguments[0].click();", add_note_button[0])
            add_note_button.click()
            time.sleep(1)
            add_text_area = driver.find_element(By.ID, "custom-message")
            if add_text_area:
                add_text_area.clear()
            add_text_area.send_keys(note_message)
            time.sleep(3)
            send_button = driver.find_element(By.XPATH, ".//button[contains(@aria-label, 'Send now')]")
            send_button.click()
            print(f"{i}: ClickedSend Button" )
            time.sleep(3)

        except NoSuchElementException:

            print(f"{i}: Not Found -> Connect")

            try:
                more_button = profile_section.find_element(By.XPATH, ".//button[contains(@aria-label, 'More actions')]")
                print(f"{i}: More Button Found")
                more_button.click()
                print(f"{i}: More Button Clicked")
                more_section = driver.find_element(By.CLASS_NAME, "artdeco-dropdown__content-inner")
                print(f"{i}: More Dropdown Found")
                connect_button = more_section.find_element(By.XPATH, "//span[contains(text(), 'Connect')]")
                print(f"{i}: Connect button in more DropdownMore Dropdown Found")

                
            except NoSuchElementException:
                print(f"{i}: Not Found! -> More")
                continue


print("Connection requests sent successfully!")

driver.quit()
