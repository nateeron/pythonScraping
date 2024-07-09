import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
async def scrape_website(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Check if the request was successful (status code 200)
            if response.status == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(await response.text(), 'html.parser')
                
                app_names = [link.get_text() for link in soup.find_all(class_="apphub_AppName")]
                discounted_prices = [link.get_text() for link in soup.find_all(class_="discount_final_price")]
                
                # Extract purchase prices, handling decimals
                purchase_prices = []
                for link in soup.find_all(class_="game_purchase_price"):
                    price_text = link.get_text().replace("฿", "").replace(",", "").replace("\r", "").replace("\n", "").replace("\t", "")
                    try:
                        price = float(price_text)
                    except ValueError:
                        price = None
                    purchase_prices.append(price)

                # Print app names, discounted final prices, and purchase prices together
                for app_name, discounted_price, purchase_price in zip(app_names, discounted_prices, purchase_prices):
                    print("App Name:", app_name)
                    print("Discounted Final Price:", discounted_price)
                    if purchase_price is not None:
                        print("Purchase Price:", purchase_price)
                    else:
                        print("Purchase Price: N/A")
                    print()  # Add an empty line for better readability between entries
                
            else:
                print("Failed to retrieve page:", response.status)

# List of URLs to scrape
urls = [
    "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/",
    # "https://store.steampowered.com/app/1551360/Forza_Horizon_5/",
    "https://store.steampowered.com/app/2344520/Diablo_IV/"
]
#scrape_website("https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/")
# Asynchronous function to run the scraping tasks concurrently
async def scrape_all():
    tasks = [scrape_website(url) for url in urls]
    await asyncio.gather(*tasks)

    # Add delay between each task
    for _ in urls[:-1]:
        await asyncio.sleep(3)

# Run the asynchronous function
asyncio.run(scrape_all())
