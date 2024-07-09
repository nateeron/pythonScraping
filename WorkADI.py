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
        print("soup : ",soup)
        
        # for link in soup.find_all(id="appHubAppName"):
        #     purchase_price = link.get_text()
        #     print("Purchase Price:", purchase_price)
        # # for link in soup.find_all(class_="game_purchase_price price"):
        # #     print("Text:", link.get_text().strip().replace("\r", "").replace("\n", "").replace("\t", ""))
        # for link in soup.find_all(class_="game_area_purchase_game_wrapper"):
        #     print("Text:", link.get_text().strip().replace("\r", "").replace("\n", "").replace("\t", "").replace("Add to Cart", ""))
        
      
    else:
        print("Failed to retrieve page:", response.status_code)



# https://www.linkedin.com/company/thai-airways-international/about/
# https://www.linkedin.com/company/qatar-airways/about/

# ค้นหา บุคคน
# https://www.linkedin.com/search/results/people/?keywords=adi&origin=SWITCH_SEARCH_VERTICAL&sid=we6
# กรองข้อมูงทำงาน Google
# 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&keywords=adi&origin=FACETED_SEARCH&sid=!T~'
# for item in urls:
#     scrape_website(item)
urlLinkedIN = 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&keywords=adi&origin=FACETED_SEARCH&sid=!T~'
scrape_website(urlLinkedIN)