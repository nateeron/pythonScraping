import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def scrape_website(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Check if the request was successful (status code 200)
            if response.status == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(await response.text(), 'html.parser')
                
                # Find and print app names
                for linka in soup.find_all(class_="apphub_AppName"):
                    print("App Name:", linka.get_text())
                
                # Find and print discount percentages
                for linkd in soup.find_all(class_="discount_pct"):
                    print("Discount Percentage:", linkd.get_text())
                
                # Find and print discounted final prices
                for linkf in soup.find_all(class_="discount_final_price"):
                    print("Discounted Final Price:", linkf.get_text())
                
            else:
                print("Failed to retrieve page:", response.status)

# List of URLs to scrape
urls = [
    "https://store.steampowered.com/app/1817070/Marvels_SpiderMan_Remastered/",
    "https://store.steampowered.com/app/1551360/Forza_Horizon_5/"
]

# Asynchronous function to run the scraping tasks concurrently
async def scrape_all():
    tasks = [scrape_website(url) for url in urls]
    await asyncio.gather(*tasks)

# Run the asynchronous function
asyncio.run(scrape_all())


