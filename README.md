# Finance Scrapers
A pypi package to scrape stock information from different finance sites. Currently supports [Yahoo Finance](finance.yahoo.com).

## Installation
To install, [Download the PyPi package](https://pypi.org/project/finance-scrapers/0.0.2/#files) _or_,
```
pip install finance-scrapers
```
To upgrade to the latest version,
```
pip install --upgrade finance-scrapers
```

## Usage
Scrape stock information:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

# run the scraper
scraper = YahooFinance(tickers)
all_stock_info = scraper.stock_info
```

<br>

Scrape stock information and __display__ to terminal:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

# display data found from stocks
scraper = YahooFinance(tickers)
scraper.display_data()

# display custom data
sample_data = {"name": "Mandy-cyber", "love": "food"}
scraper.display_data(sample_data)
```

<details>
    <summary>Example</summary>

    {
        "SCHB": {
            "Current Price": "51.17",
            "Previous Close": "50.88",
            "Avg Volume": "2009-11-03",
            "PE Ratio (TTM)": "50.87",
            "Bid": "51.10 x 3200",
            "52 Week Range": "40.92 - 53.71",
            "Open": "50.99",
            "Yield": "1.42%",
            "Day's Range": "50.74 - 51.18",
            "YTD Daily Total Return": "14.40%",
            "Beta (5Y Monthly)": "1.01",
            "Volume": "706,955",
            "Net Assets": "23.86B",
            "Ask": "51.11 x 1300"
        },
        "GOOGL": {
            "Current Price": "128.69",
            "Previous Close": "127.46",
            "Avg Volume": "147.79",
            "PE Ratio (TTM)": "1.06",
            "Bid": "128.39 x 1300",
            "52 Week Range": "83.34 - 133.74",
            "Open": "127.18",
            "EPS (TTM)": "4.40",
            "Day's Range": "126.56 - 128.73",
            "Earnings Date": "Oct 23, 2023 - Oct 27, 2023",
            "Forward Dividend & Yield": "N/A (N/A)",
            "Volume": "14,563,877",
            "Market Cap": "1.636T",
            "Ask": "128.37 x 1100"
        },
        "NKE": {
            "Current Price": "103.01",
            "Previous Close": "104.81",
            "Avg Volume": "116.24",
            "PE Ratio (TTM)": "1.12",
            "Bid": "102.84 x 800",
            "52 Week Range": "82.22 - 131.31",
            "Open": "105.47",
            "EPS (TTM)": "3.23",
            "Day's Range": "102.63 - 105.48",
            "Earnings Date": "Sep 27, 2023 - Oct 02, 2023",
            "Forward Dividend & Yield": "1.36 (1.29%)",
            "Volume": "4,524,728",
            "Market Cap": "158.325B",
            "Ask": "102.86 x 1000"
        }
    }


</details>

<br>

Scrape stock information and __download__ to a file:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

scraper = YahooFinance(tickers)

# download data
scraper.download_data(file_type="json", file_path="sample.json", overwrite=False) # or,
scraper.download_data("markdown", "sample.md") # or,
scraper.download_data("csv", "sample.csv") # or,
scraper.download_data("excel", "sample.xlsx")
```

<sub>Examples of these downloads can be found <a href="https://github.com/Mandy-cyber/Finance-Scrapers/tree/main/samples">here</a></sub>

<br>
