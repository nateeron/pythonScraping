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
        
        for link in soup.find_all(id="appHubAppName"):
            purchase_price = link.get_text()
            print("Purchase Price:", purchase_price)
        # for link in soup.find_all(class_="game_purchase_price price"):
        #     print("Text:", link.get_text().strip().replace("\r", "").replace("\n", "").replace("\t", ""))
        for link in soup.find_all(class_="game_area_purchase_game_wrapper"):
            print("Text:", link.get_text().strip().replace("\r", "").replace("\n", "").replace("\t", "").replace("Add to Cart", ""))
        
      
    else:
        print("Failed to retrieve page:", response.status_code)

# Example usage:
url = "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/"
#scrape_website(url)

urls = [
    "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/",
    "https://store.steampowered.com/app/1551360/Forza_Horizon_5/",
    "https://store.steampowered.com/app/2344520/Diablo_IV/",
    "https://store.steampowered.com/app/1650010/RIDE_5/",
    "https://store.steampowered.com/app/1850570/DEATH_STRANDING_DIRECTORS_CUT/",
    "https://store.steampowered.com/app/2231380/Tom_Clancys_Ghost_Recon_Breakpoint/",
    "https://store.steampowered.com/app/2208920/Assassins_Creed_Valhalla/",
    "https://store.steampowered.com/app/812140/",
    "https://store.steampowered.com/app/690790/DiRT_Rally_20/",
]
for item in urls:
    scrape_website(item)