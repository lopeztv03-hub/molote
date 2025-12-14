# Selenium Learning Guide

## What You'll Learn

1. **Waits** — How to wait for elements before interacting
   - Explicit waits (recommended)
   - Expected conditions (title, presence, visibility, clickable)
   - Timeout handling

2. **Selectors** — How to find elements on a page
   - CSS selectors (most common)
   - XPath (powerful for complex logic)
   - By Tag, ID, Class, etc.

3. **Interactions** — How to click, type, and extract data
   - `.text` — Get element text
   - `.get_attribute()` — Get attributes like href, class, id
   - `.click()` — Click elements
   - `.send_keys()` — Type text
   - `.is_displayed()` — Check visibility

4. **Error Handling** — How to handle failures gracefully
   - `TimeoutException` — Element didn't appear
   - `NoSuchElementException` — Element not found
   - Try/except blocks

## Files to Study

- **Basic Selenium**: `selenium_learning.py`
  - Covers waits, selectors, element interactions
  - Uses standard Selenium (all Python versions)
  
- **UC with Error Handling**: `uc_learning.py`
  - Covers undetected_chromedriver patterns
  - Shows error handling best practices
  - Requires Python 3.11

## Quick Run

**Selenium Learning (Python 3.14):**
```powershell
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv/Scripts/python.exe "C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/TikTok-Follow-Heart-Views-Bot-main/selenium_learning.py"
```

**UC Learning (Python 3.11):**
```powershell
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv311/Scripts/python.exe "C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/TikTok-Follow-Heart-Views-Bot-main/uc_learning.py"
```

## Key Patterns to Memorize

### Wait for an element to appear
```python
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button.submit"))
)
```

### Find elements
```python
# By CSS selector
element = driver.find_element(By.CSS_SELECTOR, ".class-name")

# By XPath
element = driver.find_element(By.XPATH, "//button[@id='submit']")

# By ID
element = driver.find_element(By.ID, "submit-button")
```

### Interact with elements
```python
# Click
element.click()

# Type text
element.send_keys("username")

# Get text
text = element.text

# Get attribute
href = element.get_attribute("href")
```

### Error handling
```python
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
except TimeoutException:
    print("Element did not appear in time")
```

## Practice Ideas

1. Navigate to a news site, find article headlines, print them
2. Fill out a test form (e.g., https://formy.helpcode.com/form)
3. Search for something on Google and extract result titles
4. Take a screenshot of a page

All of these are legal, ethical, and teach real skills.
