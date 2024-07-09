import asyncio
import requests
from bs4 import BeautifulSoup
import time

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        print("------------------------------------------------------------")
   
        for link in soup.find_all(class_="DWVWOJ"):
            print(link)
            Name =  link.get_text()
            price =  link.get(class_="nW_6Oi")
            print("Name:",Name,"Price : ",price )
   
      
    else:
        print("Failed to retrieve page:", response.status_code)

# Example usage:
url = "https://shopee.co.th/user/purchase/?type=3"
#scrape_website(url)
scrape_website(url)
urls = [
    "https://shopee.co.th/user/purchase/?type=3",
]
# for item in urls:
#     scrape_website(url)
    