from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os


# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # URL of the login page
    login_url = 'https://www.linkedin.com/uas/login'
    # Open the login page
    driver.get(login_url)
    
    # Find the username field and enter the username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("")
    
    # Find the password field and enter the password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("")
    
    # Submit the form
    password_field.send_keys(Keys.RETURN)
    
    # Wait for the login to complete (you may need to adjust the sleep duration)
    time.sleep(20)
    
    # URL of the page you want to scrape after logging in
    protected_url = 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&keywords=adi&origin=FACETED_SEARCH&sid=!T~'
    
    # Navigate to the protected page
    driver.get(protected_url)
    
    # Wait for the page to load completely (adjust the sleep duration as necessary)
    time.sleep(5)
    
    # Get the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    # Extract the desired content (for demonstration, we'll save the entire HTML)
    html_content = soup.prettify()
    
    # Create a folder named 'page' if it doesn't exist
    os.makedirs('page', exist_ok=True)
    
    # Save the HTML content to a file named 'index.html' in the 'page' folder
    with open('page/index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print("HTML content saved to 'page/index.html'")
    # Extract and print the desired content
    print(soup.prettify())
    
finally:
    # Close the browser
    driver.quit()


