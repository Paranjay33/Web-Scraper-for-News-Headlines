# 📰 Web Scraper for News Headlines

This project is a Python-based web scraper that extracts the latest news headlines from [NDTV News](https://www.ndtv.com/latest) and saves them to a text file.

## 📌 Features

- Scrapes live top headlines from NDTV News.
- Uses `requests` and `BeautifulSoup` for efficient HTML parsing.
- Saves headlines in a clean, numbered format in a `.txt` file.
- Can be scheduled or extended for broader use in news aggregation.

## 🛠️ Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## 📂 Project Structure

```
D:\Internship\
│
├── webscraper.py         # Main Python script for scraping
└── headlines.txt         # Output file containing the scraped headlines
```

## ▶️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Paranjay33/Web-Scraper-for-News-Headlines.git
   cd Web-Scraper-for-News-Headlines
   ```

2. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the script**:
   ```bash
   python webscraper.py
   ```

4. **Check output**:
   Headlines will be saved to `headlines.txt` in the same folder.

## 🧪 Sample Output

```
1. Supreme Court Reserves Verdict On Electoral Bonds
2. India Likely To Face England In T20 Semi-Final
3. Heavy Rain Alert In Mumbai For Next 3 Days
...
```

## 💡 Possible Improvements

- Include article URLs
- Scrape from multiple news websites
- Schedule periodic scraping using cron or task scheduler
- Export to CSV/JSON

## 📄 License

This project is licensed for educational and non-commercial use.

---

> Developed by **Paranjay Singh Jamwal** during Python Developer Internship.
