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
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = []

# run the scraper
scraper = YahooFinance(tickers)
all_stock_info = scraper.scrape() # format = json string
```