from enum import Enum

class StockInfo(Enum):
    """
    Represents all the XPATH positions of information available about a stock
    """

    INFO_1 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]"""
        }
    
    INFO_2 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]"""
        }
    
    INFO_3 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]"""
        }
    
    INFO_4 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]"""
        }
    
    INFO_5 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]"""
        }
    
    INFO_6 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]"""
        }

    INFO_7 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]"""
        }

    INFO_8 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]"""
        }

    INFO_9 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]"""
        }

    INFO_10 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]"""
        }

    INFO_11 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]"""
        }

    INFO_12 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]"""
        }

    INFO_13 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]"""
        }

    INFO_14 = {
        "name_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]"""
        }

    INFO_15 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]"""
        }

    INFO_16 = {
        "name_loc": """//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[1]/span""", 
        "info_loc": """//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]"""
        }