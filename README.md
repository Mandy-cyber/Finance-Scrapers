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
scraper.display(sample_data)
```

<details>
    <summary>Example</summary>


    {
        "AXP": {
            "Ask": "171.39 x 800",
            "PE Ratio (TTM)": "17.95",
            "Open": "172.17",
            "Earnings Date": "Jul 21, 2023",
            "Volume": "Jul 06, 2023",
            "Market Cap": "127.169B",
            "Avg. Volume": "186.00",
            "52 Week Range": "130.65 - 182.15",
            "Forward Dividend & Yield": "2.40 (1.36%)",
            "Day's Range": "167.42 - 173.34",
            "Previous Close": "177.11",
            "EPS (TTM)": "9.53",
            "Bid": "171.28 x 1000"
        },
        "SCHB": {
            "Ask": "53.07 x 1000",
            "PE Ratio (TTM)": "21.73",
            "Open": "53.12",
            "YTD Daily Total Return": "18.99%",
            "Volume": "0.03%",
            "Net Assets": "23B",
            "Avg. Volume": "2009-11-03",
            "52 Week Range": "40.92 - 53.43",
            "Beta (5Y Monthly)": "1.01",
            "Day's Range": "52.88 - 53.12",
            "Previous Close": "52.92",
            "Yield": "1.47%",
            "Bid": "53.06 x 2200"
        },
        "NKE": {
            "Ask": "108.85 x 1800",
            "PE Ratio (TTM)": "33.80",
            "Open": "108.00",
            "Earnings Date": "Sep 27, 2023 - Oct 02, 2023",
            "Volume": "Jun 02, 2023",
            "Market Cap": "167.816B",
            "Avg. Volume": "127.70",
            "52 Week Range": "82.22 - 131.31",
            "Forward Dividend & Yield": "1.36 (1.26%)",
            "Day's Range": "107.54 - 109.24",
            "Previous Close": "107.53",
            "EPS (TTM)": "3.23",
            "Bid": "108.83 x 1200"
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