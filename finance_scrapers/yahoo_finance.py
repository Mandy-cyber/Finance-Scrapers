# external imports
import requests, concurrent.futures
from bs4 import BeautifulSoup
from typing import Dict, List
# internal imports
from finance_scrapers.downloader import Downloader


class YahooFinance:
    """
    A tool for scraping publicly available stock information from Yahoo Finance

    Attrs:
        home_url (str): the url of the home page for Yahoo Finance
    """
    home_url: str = "https://www.finance.yahoo.com"


    def __init__(self, tickers: List[str], max_threads: int = 10) -> None:
        """
        Initializes a YahooFinance to scrape information about the given stocks which
        are identified by their ticker symbols.

        Args
            tickers: the tickers of the stocks to be scraped
            max_threads: the max number of threads to use when multithreading
        """
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
        } 
        self.max_threads = max_threads

        tickers = list(map(lambda ticker: ticker.upper(), tickers))
        self.tickers = tickers
        self.all_stock_info = {}


    def find_stock_info(self, ticker: str) -> Dict[str, dict]:
        """Finds all information available about the given stock from the
        summary section of the stock's Yahoo Finance page

        Args:
            ticker: the stock's ticker
        Returns:
            a dictionary of all the information found
        """
        # get html
        url = f"{self.home_url}/quote/{ticker}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.HTTPError:
            print("TODO fix this exception situation")
            return None
        
        # parse html
        soup = BeautifulSoup(response.content, "html5lib")
        table = soup.find('div', attrs={'class': 'container yf-tx3nkj'})
        info = {}

        for row in table.find_all('li', attrs={'class': 'yf-tx3nkj'}):
            label = row.find('span', class_='label')                # attr
            value_container = row.find('span', class_='value')      # value
            
            if value_container:
                value = value_container.find('fin-streamer') or value_container
                if label and value:
                    info[label.text.strip()] = value.text.strip()

        self.all_stock_info[ticker] = info
        return { ticker: info }


    def run(self):
        """Runs the scraper, storing all stock information in self.all_stock_info"""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            executor.map(self.find_stock_info, self.tickers)


if __name__ == "__main__":
    scraper = YahooFinance(['schb', 'googl', 'nke', 'axl'])
    scraper.run()
    Downloader.download_csv(data=scraper.all_stock_info, file_path='../samples/data.csv')
    Downloader.download_excel(data=scraper.all_stock_info, file_path='../samples/data.xlsx')
    Downloader.download_json(data=scraper.all_stock_info, file_path='../samples/data.json')
    Downloader.download_md(data=scraper.all_stock_info, file_path='../samples/data.md')