from enum import Enum

class StockOption(Enum):
    """
    Represents information that can be scraped about a stock, and the associated
    XPATHs of this information on yahoo finance.
    """
    PREVIOUS_CLOSE = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]"""
    OPEN = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]"""
    BID = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]"""
    ASK = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]"""
    DAYS_RANGE = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]"""
    YEAR_WEEK_RANGE = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]"""
    VOLUME = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer"""
    AVG_VOLUME = """//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]"""
    NET_ASSETS = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]"""
    NAV = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]"""
    PE_RATIO_TTM = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]"""
    YIELD = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]"""
    YTD_DAILY_TOTAL_RETURN = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]"""
    BETA = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]"""
    NET_EXPENSE_RATIO = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]"""
    INCEPTION_DATE = """//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]"""