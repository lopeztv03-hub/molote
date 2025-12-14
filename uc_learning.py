import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Learn UC-specific patterns and robust error handling

def example_uc_with_errors():
    options = uc.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = uc.Chrome(options=options)
    try:
        driver.get("https://example.com/")
        
        # Wait with error handling
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("Example Domain"))
            print("✓ UC: Page loaded")
        except TimeoutException:
            print("✗ UC: Timeout waiting for title")
            return
        
        # Find element with error handling
        try:
            heading = driver.find_element(By.TAG_NAME, "h1")
            print(f"✓ UC: Found heading: {heading.text}")
        except NoSuchElementException:
            print("✗ UC: Heading not found")
            return
        
        # Safe attribute access
        try:
            link = driver.find_element(By.TAG_NAME, "a")
            href = link.get_attribute("href")
            if href:
                print(f"✓ UC: Link href: {href}")
            else:
                print("✗ UC: No href attribute")
        except Exception as e:
            print(f"✗ UC: Error accessing link: {e}")
            
    finally:
        try:
            driver.quit()
        except:
            pass  # Ignore shutdown errors on Windows

if __name__ == "__main__":
    print("=== UC Learning with Error Handling ===\n")
    example_uc_with_errors()
    print("\n✓ UC example completed!")
