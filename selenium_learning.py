from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example 1: Explicit Waits
# Learn how to wait for elements to appear before interacting

def example_waits():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://example.com/")
        
        # Wait up to 20 seconds for title to contain "Example Domain"
        WebDriverWait(driver, 20).until(EC.title_contains("Example Domain"))
        print("✓ Page loaded successfully")
        
        # Wait for the heading element to be present
        heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        print(f"✓ Found heading: {heading.text}")
        
    finally:
        driver.quit()

# Example 2: Finding Elements (Selectors)
# Learn CSS selectors and XPath to locate elements

def example_selectors():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://example.com/")
        
        # CSS selector
        heading = driver.find_element(By.CSS_SELECTOR, "h1")
        print(f"✓ CSS selector found: {heading.text}")
        
        # XPath
        link = driver.find_element(By.XPATH, "//a[@href]")
        href = link.get_attribute("href")
        print(f"✓ XPath found link: {href}")
        
        # Tag name
        paragraph = driver.find_element(By.TAG_NAME, "p")
        print(f"✓ Tag selector found paragraph")
        
    finally:
        driver.quit()

# Example 3: Interacting with Elements
# Learn how to click, type, and extract text

def example_interactions():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://example.com/")
        
        # Get text from element
        heading = driver.find_element(By.TAG_NAME, "h1")
        text = heading.text
        print(f"✓ Retrieved text: {text}")
        
        # Get attribute
        link = driver.find_element(By.TAG_NAME, "a")
        href = link.get_attribute("href")
        print(f"✓ Retrieved attribute: {href}")
        
        # Check if element is displayed
        is_visible = link.is_displayed()
        print(f"✓ Element visible: {is_visible}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    print("=== Selenium Learning Examples ===\n")
    
    print("1. Explicit Waits Example:")
    example_waits()
    
    print("\n2. Selectors Example:")
    example_selectors()
    
    print("\n3. Element Interactions Example:")
    example_interactions()
    
    print("\n✓ All learning examples completed!")
