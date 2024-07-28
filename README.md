# Finance Scrapers
A pypi package to scrape stock information from different finance sites. Currently supports [Yahoo Finance](finance.yahoo.com).

## Installation
To install, [Download the PyPi package](https://pypi.org/project/finance-scrapers/#files) _or_,
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
scraper.run()
all_stock_info = scraper.all_stock_info
```

<br>

Scrape stock information and __download__ to a file:
```python
from finance_scrapers import YahooFinance

# the tickers of the stocks you want to scrape
tickers = ['schb', 'googl', 'nflx']

# run the scraper
scraper = YahooFinance(tickers)
scraper.run()

# download data
Downloader.download_csv(data=scraper.all_stock_info, file_path='../samples/data.csv')
Downloader.download_excel(data=scraper.all_stock_info, file_path='../samples/data.xlsx')
Downloader.download_json(data=scraper.all_stock_info, file_path='../samples/data.json')
Downloader.download_md(data=scraper.all_stock_info, file_path='../samples/data.md')
```

<sub>Examples of these downloads can be found <a href="https://github.com/Mandy-cyber/Finance-Scrapers/tree/main/samples">here</a></sub>

<br>
