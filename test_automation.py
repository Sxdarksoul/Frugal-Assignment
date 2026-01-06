import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# NOTE: Replace with the actual path to your HTML file
# Example: "file:///C:/Users/YourName/Frugal_Assignment/index.html"
driver.get(r"C:\Users\Dell\OneDrive\Desktop\frugal assignment\index.html")

print("Page Title:", driver.title) # [cite: 113]

try:
    # --- SCENARIO A: Negative Test (Missing Last Name) [cite: 111-127] ---
    print("\n--- Running Scenario A: Negative Test ---")
    driver.find_element(By.ID, "firstName").send_keys("John")
    # Skip Last Name as requested
    driver.find_element(By.ID, "email").send_keys("john@test.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_element(By.XPATH, "//input[@value='Male']").click()
    
    # Try to click submit (Button should be disabled logic)
    submit_btn = driver.find_element(By.ID, "submitBtn")
    if not submit_btn.is_enabled():
        print("PASS: Submit button is disabled due to invalid form.")
        driver.save_screenshot("screenshot_error_state.png") # [cite: 127]
    else:
        print("FAIL: Button enabled unexpectedly.")

    # --- SCENARIO B: Positive Test [cite: 128-135] ---
    print("\n--- Running Scenario B: Positive Test ---")
    driver.refresh()
    time.sleep(1)
    
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "email").send_keys("john@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("919876543210")
    driver.find_element(By.XPATH, "//input[@value='Male']").click()
    
    # Password Logic
    driver.find_element(By.ID, "password").send_keys("StrongPass123")
    driver.find_element(By.ID, "confirmPassword").send_keys("StrongPass123")
    
    # Check Terms
    driver.find_element(By.ID, "terms").click()
    
    
    submit_btn = driver.find_element(By.ID, "submitBtn")
    
    # Submit
    if submit_btn.is_enabled():
        submit_btn.click()
        print("Clicked Submit...")
        time.sleep(1) # Wait for alert
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()
        driver.save_screenshot("screenshot_success_state.png") # [cite: 135]
        print("PASS: Registration Successful.")
    
    # --- SCENARIO C: Logic Validation (Dropdowns) [cite: 136-138] ---
    print("\n--- Running Scenario C: Logic/Dropdown Test ---")
    driver.refresh()
    time.sleep(1)
    
    country_dd = Select(driver.find_element(By.ID, "country"))
    country_dd.select_by_visible_text("India")
    time.sleep(0.5)
    
    state_dd = Select(driver.find_element(By.ID, "state"))
    # Verify States updated
    options = [o.text for o in state_dd.options]
    if "Maharashtra" in str(options):
        print("PASS: State dropdown updated correctly for India.")
    else:
        print("FAIL: State dropdown did not update.")

except Exception as e:
    print("Test Failed:", e)

finally:
    time.sleep(10)  # Keeps the browser open for 10 seconds before closing
    driver.quit()