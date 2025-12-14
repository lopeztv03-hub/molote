import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyfiglet
from os import system
from time import sleep
import sys

chrome_options = uc.ChromeOptions()
#chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-features=IsolateOrigins,site-per-process')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')

# Let undetected_chromedriver manage the driver to reduce detection; keep a custom path available if needed
driver = uc.Chrome(options=chrome_options)

i = 0

def loop1():
    global i
    wait = WebDriverWait(driver, 60)
    while True:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='sid4']/div/div/div/form/div/input")))
            input_box = driver.find_element(By.XPATH, "//*[@id='sid4']/div/div/div/form/div/input")
            input_box.clear()
            input_box.send_keys(vidUrl)
            driver.find_element(By.XPATH, "//*[@id='sid4']/div/div/div/form/div/div/button").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='c2VuZC9mb2xsb3dlcnNfdGlrdG9V']/div[1]/div/form/button")))
            driver.find_element(By.XPATH, "//*[@id='c2VuZC9mb2xsb3dlcnNfdGlrdG9V']/div[1]/div/form/button").click()
            driver.refresh()
            i += 1
            total = i * 1000
            print("Views success delivered! Total", total, "views")
            sleep(55)
        except Exception as e:
            print("Waiting for page/captcha or element, retrying:", e)
            driver.refresh()
            sleep(15)
            continue

def loop2():
    sleep(10)
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
        sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element(By.XPATH, "//*[@id='c2VuZE9nb2xsb3dlcnNfdGlrdG9r']/span").text
        sleep(55)
        print(hearts," Success delivered!")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("An error occured. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    pass

def loop4():
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(20)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='sid']/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element(By.XPATH, "//*[@id='c2VuZF9mb2xsb3dlcnNfdGlrdG9r']/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("An error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4()

vidUrl = "https://www.tiktok.com/@cirumtv/photo/7582521253030907150" #Change with one of your tiktok videos

system("cls") #If you have Windows you can use cls
tiktokbot = pyfiglet.figlet_format("NoNameoN", font="slant")
print(tiktokbot)
print("Author: https://github.com/NoNameoN-A")
print("")

"""
You can change auto value below
auto = 1 for auto views OK
auto = 2 for auto hearts OK
auto = 3 for auto views + hearts InWork...
auto = 4 for auto followers OK
"""
bot = 1 #Change this

driver.get("https://vipto.de/")

# Give you a chance to solve captcha / open the page fully before automation starts
input("Solve any captcha on the opened Chrome window, ensure the page is visible, then press Enter here to start...\n(If the page stays blank, wait ~15s, then press Enter anyway to capture diagnostics.) ")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    pass
else:
    loop4()
    pass

