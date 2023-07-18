# type: ignore
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Dict, List
import progressbar
import json
import time
# internal imports
# from finance_scrapers.stock_info import StockInfo
from finance_scrapers.stock_info import StockInfo


class YahooFinance:
    """
    A tool for scraping publicly available stock information from Yahoo Finance

    Attrs:
        home_url (str): the url of the home page for Yahoo Finance
    """
    home_url: str = "https://www.finance.yahoo.com"

    def __init__(self, tickers: List[str], validate_tickers: bool = True, 
                 show_progress: bool = False, info_to_find: set[StockInfo] = set(StockInfo)) -> None:
        """
        Initializes a YahooFinance to scrape information about the given stocks
        (identified by their tickers).

        Args
            tickers: the tickers of the stocks to be scraped
            validate_tickers: if the tickers should be validated before scraping
            show_progress: if the stock-scraping progress should be displayed in the terminal
        """
        self.show_progress = show_progress
        self.tickers: List[str] = self.__validate_tickers(tickers) if validate_tickers else tickers
        self.validate_tickers = validate_tickers

        self.info_to_find = info_to_find
        self.num_options = len(info_to_find)

        self.browser = self.__configure_browser()
    
    @staticmethod
    def __create_progress_bar(progress_message: str, max_value: int) -> progressbar:
        """
        Creates an animated progress bar displaying the given message, and with a length of
        the given max.

        Args:
            progress_message: the message to be printed in the terminal

        Returns:
            progress_bar: an updatable progress bar
        """
        widgets = [
            f"{progress_message}: ", 
            progressbar.AnimatedMarker(),
            progressbar.Bar('*'),
            ' [', progressbar.ETA(), ']\n',
            ]
        
        progress_bar = progressbar.ProgressBar(max_value=max_value, widgets=widgets)
        return progress_bar
    

    def __explicit_wait(self, search_method: By, element: str, max_wait_time: int = 2) -> str:
        """
        Explicitly waits for the given element to be located on the browser's page
        before proceeding to gather its value.

        Args
            element: the element whose presence is being awaited
            max_wait_time: the amount of time to wait before 'giving up' finding the element
        
        Returns:
            element_value: the value of the element (i.e. the information stored in it) or
                           "N/A" if the element could not be found.
        """
        element_value: str
        try:
            element_value = WebDriverWait(self.browser, max_wait_time).until(
                EC.presence_of_element_located((search_method, element))
            ).text
        except:
            element_value = "N/A"
        return element_value
    

    def __valid_ticker(self, ticker: str) -> bool:
        """
        Determines if the given ticker is valid--i.e. 5 or fewer characters

        Args
            ticker: the ticker to validate
        
        Returns
            True if valid, False if invalid
        """
        ticker_len = len(ticker)
        return ticker_len <= 5 and ticker_len > 0

    
    def __validate_tickers(self, tickers: List[str]) -> List[str]:
        """
        Determines if the given stock tickers are valid--i.e. 5 or fewer
        characters.

        Args:
            tickers: the list of stock tickers to validate

        Returns:
            valid_tickers: the list of valid tickers, if any
        """
        valid_tickers: List[str] = []

        for idx, ticker in enumerate(tickers):
            ticker = ticker.upper()
            valid_ticker = [ticker] if self.__valid_ticker(ticker) else self.__request_new_ticker(ticker)
            valid_tickers.extend(valid_ticker)

        return valid_tickers
    

    def __request_new_ticker(self, invalid_ticker: str) -> List[str]:
        """
        Asks the user via the terminal for a new ticker to replace the
        invalid one.

        Args
            invalid_ticker: the invalid ticker originally provided by the user

        Returns
            valid_ticker: empty if no replacement given, one-element list if
                          valid replacement provided
        """
        request_new = input(f"The provided ticker {invalid_ticker} is invalid. Would you like to choose another (y/n)?:  ")
        if request_new.lower() == "n":
            return []
        
        valid_ticker: List[str] = []
        valid_provided = False

        while not valid_provided:
            new_ticker = input(f"New ticker: ").upper()
            # valid provided
            if self.__valid_ticker(new_ticker):
                valid_ticker.append(new_ticker)
                break
            else:
                # ask again
                valid_ticker = self.__request_new_ticker(new_ticker)
            
        return valid_ticker
    

    def __configure_browser(self) -> webdriver:
        """
        Downloads (if one doesn't already exist) and configures a ChromeDriver with basic options, 
        then navigates to the Yahoo Finance home page.

        Returns:
            browser: the configured webdriver on finance.yahoo.com
        """
        get_driver = GetChromeDriver()
        get_driver.install()

        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("--log-level=3")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=chrome_options)

        browser.get(YahooFinance.home_url)
        # wait for page to load
        self.__explicit_wait(By.ID, "yfin-usr-qry")
        return browser
    

    def __find_stock(self, ticker: str) -> None:
        """
        Navigates to the given stock's (represented by its ticker) summary page

        Arg:
            ticker: the ticker of the stock being found
        """
        searchbar = self.browser.find_element(By.ID, "yfin-usr-qry")
        searchbar.send_keys(ticker)
        searchbar.send_keys(Keys.RETURN)
        # waits for stock header to be found (i.e. page has been loaded)
        self.__explicit_wait(By.ID, "quote-header-info")


    def __get_stock_info(self, ticker: str) -> Dict[str, str]:
        """
        Gathers all information, requested by the user, about the given stock

        Args:
            ticker: the ticker of the stock whose info is being gathered

        Returns:
            stock_info: information about the stock
        """
        self.__find_stock(ticker)
        stock_info: Dict[str, str] = dict()
        
        for idx, info in enumerate(self.info_to_find):
            info_val = info.value
            info_name = self.__explicit_wait(By.XPATH, info_val['name_loc'])
            info_text = self.__explicit_wait(By.XPATH, info_val['info_loc'])
            stock_info[info_name] = info_text

        return stock_info
    

    def __find_stocks(self) -> Dict[str, Dict[str, str]]:
        """
        Finds all the stocks, with their information, requested by the user

        Returns:
            all_stocks_info: keys = the stock names  |  values = the stock information
        """
        all_stocks_info: Dict[str, Dict[str, str]] = dict()

        for idx, ticker in enumerate(self.tickers): 
            all_stocks_info[ticker] = self.__get_stock_info(ticker)

        return all_stocks_info

    def scrape(self) -> str:
        """
        Runs the scraper to find all the stock information then displays the results
        in json string format.

        Returns
            formatted_info: the stocks' information in json string format
        """
        stock_info = self.__find_stocks()
        formatted_info = json.dumps(stock_info, indent=4)
        print(formatted_info)
        return formatted_info