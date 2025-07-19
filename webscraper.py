import requests
from bs4 import BeautifulSoup

# Target URL (You can change this to any news site you prefer)
url ='https://www.ndtv.com/latest'

# Define headers to simulate a real browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

try:
    # Fetch HTML content
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status

    # Parse the content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract headlines (e.g., h3 tags with certain class names)
    headlines = soup.find_all(['h1', 'h2', 'h3'])

    # Save the headlines in a .txt file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for index, headline in enumerate(headlines, start=1):
            text = headline.get_text(strip=True)
            if text:  # Avoid empty strings
                file.write(f"{index}. {text}\n")

    print("Headlines scraped and saved to 'headlines.txt'.")

except Exception as e:
    print("An error occurred:", e)
