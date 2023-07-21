# external imports
# type: ignore
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Dict, List
import progressbar
import json
# internal imports
# from finance_scrapers.stock_info import StockInfo
# from finance_scrapers.downloader import Downloader
from stock_info import StockInfo
from downloader import Downloader


class YahooFinance:
    """
    A tool for scraping publicly available stock information from Yahoo Finance

    Attrs:
        home_url (str): the url of the home page for Yahoo Finance
    """
    home_url: str = "https://www.finance.yahoo.com"

    def __init__(self, tickers: List[str], validate_tickers: bool = True, 
                 show_progress: bool = False) -> None:
        """
        Initializes a YahooFinance to scrape information about the given stocks which
        are identified by their ticker symbols. Found information is stored in self.stock_info

        Args
            tickers: the tickers of the stocks to be scraped
            validate_tickers: if the tickers should be validated before scraping
            show_progress: if the stock-scraping progress should be displayed in the terminal
        """
        # general
        tickers = map(lambda ticker: ticker.upper(), tickers)
        self.browser = YahooFinance.__configure_browser()
        self.info_to_find = set(StockInfo)
        self.show_progress = show_progress

        # find stocks straight away if validation doesn't matter
        self.stock_info: Dict[str, Dict[str, str]] = dict() if validate_tickers else self.find_stocks(tickers)

        # validate stocks and then automatically find stock information as validation occurs
        self.validate_tickers = validate_tickers
        self.tickers: List[str] = self.check_tickers(tickers) if validate_tickers else tickers

        
        
    
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
    

    def _explicit_wait(self, search_method: By, element: str, max_wait_time: int = 2) -> str:
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
    

    def valid_ticker(self, ticker: str) -> bool:
        """
        Determines if the given ticker is valid--i.e. 5 or fewer characters and exists
        on yahoo finance. Will scrape the information and store if valid.

        Args:
            ticker: the ticker to validate
        
        Returns:
            True if valid, False if invalid
        """
        ticker_len = len(ticker)
        stock = self.get_stock_info(ticker)

        valid = (ticker_len <= 5 and ticker_len > 0) and (stock != dict())
        if valid:
            self.stock_info[ticker] = stock

        return valid

    
    def check_tickers(self, tickers: List[str]) -> List[str]:
        """
        Determines if the given stock tickers are valid--i.e. 5 or fewer
        characters and exists on yahoo finance.

        Args:
            tickers: the list of stock tickers to validate

        Returns:
            valid_tickers: the list of valid tickers, if any
        """
        valid_tickers: List[str] = []

        for ticker in tickers:
            valid_ticker = [ticker] if self.valid_ticker(ticker) else self.__request_new_ticker(ticker)
            valid_tickers.extend(valid_ticker)

        return valid_tickers
    

    def __request_new_ticker(self, invalid_ticker: str) -> List[str]:
        """
        Asks the user via the terminal for a new ticker to replace the
        invalid one.

        Args:
            invalid_ticker: the invalid ticker originally provided by the user

        Returns:
            valid_ticker: empty if no replacement given, one-element list if
                          valid replacement provided

        Raises:
            ValueError: if an invalid response to the 'request new ticker' question
                        is provided.
        """
        request_new = input(f"The provided ticker {invalid_ticker} is invalid/does not exist. Would you like to choose another (y/n)?:  ")
        # dont choose new ticker
        if request_new.lower() == "n":
            return []
        elif request_new.lower() != "y":
            raise ValueError("Invalid response provided. Expected either 'y' or 'n'")

        # choose new ticker
        valid_ticker: List[str] = []
        valid_provided = False

        while not valid_provided:
            new_ticker = input(f"New ticker: ").upper()
            # valid provided
            if self.valid_ticker(new_ticker):
                valid_ticker.append(new_ticker)
                break
            else:
                # ask again
                valid_ticker = self.__request_new_ticker(new_ticker)
            
        return valid_ticker
    

    @staticmethod
    def __configure_browser() -> webdriver:
        """
        Downloads (if one doesn't already exist) and configures a ChromeDriver with basic options.

        Returns:
            browser: the configured webdriver on finance.yahoo.com
        """
        get_driver = GetChromeDriver()
        get_driver.install()

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("--log-level=3")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome(options=chrome_options)
        return browser
    

    def __find_stock(self, ticker: str) -> bool:
        """
        Navigates to the given stock's (represented by its ticker) summary page. If
        a value that is not an actual stock ticker is provided, yahoo finance will
        navigate to a 'lookup' page, indicating to us that the stock could not be found.

        Arg:
            ticker: the ticker of the stock being found

        Returns:
            True if the stock could be found, False otherwise
        """
        url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"
        self.browser.get(url)
        if self.stock_exists(expected_url=url):
            self._explicit_wait(By.ID, "quote-header-info")
            return True
        
        return False


    def stock_exists(self, expected_url: str) -> bool:
        """
        Checks whether the stock exists by comparing the expected url of the stock's
        summary page, with the browser's current url. If they do not match, the stock
        does not exist.

        Args:
            expected_url: the expected yahoo finance page link if the stock exists

        Returns:
            True if the stock exists, False otherwise
        """
        current_url = self.browser.current_url
        return current_url == expected_url


    def get_stock_info(self, ticker: str) -> Dict[str, str]:
        """
        Gathers all information, requested by the user, about the given stock,
        if it could be found.

        Args:
            ticker: the ticker of the stock whose info is being gathered

        Returns:
            stock_info: information about the stock
        """
        stock_info: Dict[str, str] = dict()

        if self.__find_stock(ticker):
            for info in self.info_to_find:
                # get information
                info_val = info.value
                info_name = self._explicit_wait(By.XPATH, info_val['name_loc'])
                info_text = self._explicit_wait(By.XPATH, info_val['info_loc'])
                # store information
                stock_info[info_name] = info_text
                
        return stock_info
    

    def find_stocks(self, tickers: List[str]) -> Dict[str, Dict[str, str]]:
        """
        Finds all the stocks, with their information, requested by the user

        Args:
            tickers: the tickers of the stocks to find
        
        Returns:
            all_stocks_info: keys = the stock names  |  values = the stock information
        """
        all_stocks_info: Dict[str, Dict[str, str]] = dict()

        for ticker in tickers: 
            all_stocks_info[ticker] = self.get_stock_info(ticker)

        return all_stocks_info
    

    def display_data(self, data: Dict = None) -> None:
        """
        Displays the given data in the terminal as 'pretty' json. Defaults
        to displaying data about the stocks scraped.

        Args:
            data: the data to be displayed in the terminal
        """
        if data != None:
            print(json.dumps(data, indent=4))
        else:
            print(json.dumps(self.stock_info, indent=4))
    

    def download_data(self, file_type: str, file_path: str, overwrite: bool = True) -> None:
        """
        Download's the given stock information to a file of the given type.

        File Type options: 
            - json
            - csv
            - markdown
            - excel

        Args:
            file_type: the type of file to download the data to
            file_path: where the file is located/should be downloaded to
            overwrite: if the file should be overwritten if it already exists

        Raises:
            ValueError: if an invalid/unsupported file type is provided or if
                        attempting to download a file of one type using a different
                        method (e.g. markdown in sample.json)
        """
        downloader = Downloader(
            self.stock_info, 
            file_path=file_path,
            overwrite=overwrite
        )

        download_methods = {
            "json": downloader.download_json,
            "csv": downloader.download_csv,
            "excel": downloader.download_excel,
            "markdown": downloader.download_md
        }
        supported_file_types = download_methods.keys()
        
        if file_type.lower() not in supported_file_types:
            raise ValueError("Invalid file type provided. Expected one of: %s" % supported_file_types)
        else:
            download_methods[file_type]()
