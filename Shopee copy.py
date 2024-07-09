import requests
from bs4 import BeautifulSoup

def login_and_scrape(url, login_url, credentials):
    with requests.Session() as session:
        # Retrieve login page
        session.get(login_url)

        # Add headers to simulate a real user
        headers = {
            'User-Agent': 'Mozilla/5.0',
        }

        # Attempt to login
        response = session.post(login_url, data=credentials, headers=headers)
        
        # Check if login was successful by looking for a specific element or URL redirection
        # This step varies greatly by website and may require inspecting network requests

        # Access the target page after login
        print("-----url---------headers----------------------------------------------")
        
        print(url)
        print(headers)
        
        response = session.get(url, headers=headers)
        with open('response.txt', 'w', encoding='utf-8') as file:
            file.write(str(response))
        print("-----------------response-------------------------------------------")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Perform scraping actions here
            #print(soup.prettify())
            with open('prettify.txt', 'w', encoding='utf-8') as file:
                file.write(str(soup.prettify()))
            print("------------------------------------------------------------")
            for link in soup.find_all(class_="tv-widget-idea__title-row"):
                print(link)
                Name =  link.get_text()
                price =  link.find(class_="tv-widget-idea__title apply-overflow-tooltip")
                print("Name:",Name,"Price : ",price )
            else:
                print("Failed to retrieve page after login:", response.status_code)
#https://www.tradingview.com/scripts/?script_type=strategies
#https://www.tradingview.com/script/4J80gPhd-FreedX-Grid-Backtest/#chart-view-comment-form

# Credentials should be in the form expected by the login form, typically including usernames and passwords
credentials = {
    'username': '0949314443',
    'password': 'C4544142z-*/1122'
}

# URLs
login_url = "https://shopee.co.th/buyer/login"
target_url = "https://www.tradingview.com/scripts/?script_type=strategies"

# Execute scraping
login_and_scrape(target_url, login_url, credentials)
