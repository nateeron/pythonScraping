import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for link in soup.find_all("#appHubAppName"):
            print("Name:", link.get_text())
        for linkdiscount_pct in soup.find_all(class_="discount_pct"):
            print("Discount Pct:", linkdiscount_pct.get_text())
        for linkprice in soup.find_all(class_="discount_final_price"):
            print("Final Price:", linkprice.get_text())
        for linkpurchaseprice in soup.find_all(class_="game_purchase_price"):
            ss = int(linkpurchaseprice.get_text().replace("฿","").replace(",","").replace("\r","").replace("\n","").replace("\t",""))
            print("Purchase Price:", ss)
        
    else:
        print("Failed to retrieve page:", response.status_code)

# Example usage:
url = "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/"
scrape_website(url)


#url = "https://store.steampowered.com/app/1551360/Forza_Horizon_5/"
#scrape_website(url)