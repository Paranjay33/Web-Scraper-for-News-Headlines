import requests
from bs4 import BeautifulSoup
url ='https://www.ndtv.com/latest'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

try:
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h1', 'h2', 'h3'])

    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for index, headline in enumerate(headlines, start=1):
            text = headline.get_text(strip=True)
            if text: 
                file.write(f"{index}. {text}\n")

    print("Headlines scraped and saved to 'headlines.txt'.")

except Exception as e:
    print("An error occurred:", e)
