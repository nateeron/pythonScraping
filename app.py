import requests
from bs4 import BeautifulSoup



def ConvertTack(tack):
    resp = str(tack).replace('[1]',':nth-of-type(1)')
    resp = resp.replace('[2]',':nth-of-type(2)')
    resp = resp.replace('[3]',':nth-of-type(3)')
    resp = resp.replace('[4]',':nth-of-type(4)')
    resp = resp.replace('[5]',':nth-of-type(5)')
    resp = resp.replace('[6]',':nth-of-type(6)')
    resp = resp.replace('[7]',':nth-of-type(7)')
    resp = resp.replace('[8]',':nth-of-type(8)')
    resp = resp.replace('[9]',':nth-of-type(9)')
    resp = resp.replace('[10]',':nth-of-type(10)')
    resp = resp.replace('[11]',':nth-of-type(11)')
    resp = resp.replace('[12]',':nth-of-type(12)')
    resp = resp.replace('[13]',':nth-of-type(13)')
    resp = resp.replace('[14]',':nth-of-type(14)')
    resp = resp.replace('[15]',':nth-of-type(15)')
    resp = resp.replace('[16]',':nth-of-type(16)')
    resp = resp.replace('[17]',':nth-of-type(17)')
    resp = resp.replace('[18]',':nth-of-type(18)')
    resp = resp.replace('[19]',':nth-of-type(19)')
    resp = resp.replace('[20]',':nth-of-type(20)')
    resp = resp.replace('[21]',':nth-of-type(21)')
    resp = resp.replace('[22]',':nth-of-type(22)')
    resp = resp.replace('[23]',':nth-of-type(23)')
    resp = resp.replace('[24]',':nth-of-type(24)')
    resp = resp.replace('[25]',':nth-of-type(25)')
    resp = resp.replace('[26]',':nth-of-type(26)')
    resp = resp.replace('[27]',':nth-of-type(27)')
    resp = resp.replace('[28]',':nth-of-type(28)')
    resp = resp.replace('[29]',':nth-of-type(29)')
    resp = resp.replace('[30]',':nth-of-type(30)')
    return resp
 
 
 
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Here, you can write your scraping logic
        # For example, let's extract all the <a> tags and print their text and href attributes
        # for link in soup.find_all('p'):
        #     print("Text:", link.get_text(), "URL:", link.get('href'))
        
        #for link in soup.find_all(class_="price-home2"):
        for link in soup.find_all(class_="page-item"):
            print("Text:", link.get_text(), "URL:", link.get('href'))
        
        # for h2_tag in soup.select('/html/body/div/article/main/div/h2'):
        #     print("Text:", h2_tag.get_text())
        # data = '/html/body/div[6]/div/div/div[1]/a/div/div[1]/div[1]/small'
        
        # data = ConvertTack(data.replace('/html/','').replace('/',' > '))
        # print(data)
        # for h2_tag in soup.select(data):
        #     print("Text:", h2_tag.get_text())
    else:
        print("Failed to retrieve page:", response.status_code)

# Example usage:
url = "https://www.interhome.co.th/result.php?resulttype=Search&proptype=&province=&district=&street=&price=&keyword=&plocate=both&propsell=Y&proprent=Y"
scrape_website(url)



