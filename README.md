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
Scrape stock information and __display__ to terminal:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

# run the scraper
scraper = YahooFinance(tickers)
all_stock_info = scraper.stock_info
```

<br>

Scrape stock information and __download__ to a file:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

scraper = YahooFinance(tickers)

# download data
scraper.download_data("json", "sample.json", overwrite=False) # or,
scraper.download_data("markdown", "sample.md") # or,
scraper.download_data("csv", "sample.csv") # or,
scraper.download_data("excel", "sample.xlsx")
```
