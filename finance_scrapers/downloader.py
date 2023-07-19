import os
import pandas as pd # type: ignore

class Downloader:
    """Represents a tool for downloading a dictionary of data to a file."""

    def __init__(self, data_dict: dict, file_path: str, overwrite: bool = True) -> None:
        """
        Initializes a downloader to download the data in the given dictionary

        Args:
            data_dict: a dictionary of data to download to a file
            file_path: the path to the file to download to
            overwrite: if the file should be overwritten if it already exists. 
                       Otherwise a new file path is automatically generated
        """
        self.data_dict = data_dict
        self.overwrite = overwrite
        self.file_path = file_path if overwrite else Downloader.generate_file_path(file_path)
        

    @staticmethod
    def generate_file_path(file_path: str) -> str:
        """
        Generates a new file path if the one at the given path already exists,
        or returns the same path if it does not exist. 

        E.x. if sample.txt exists then it will be changed to sample(1).txt

        Args:
            file_name (str): _description_

        Returns:
            file_path: the new file path
        """
        file_exists = os.path.isfile(file_path)

        if file_exists:
            file_split = os.path.splitext(file_path)
            file_name = file_split[0]
            file_extension = file_split[1]

            # change file path until unique
            accum = 1
            while file_exists:
                new_path = file_name + f"({accum}){file_extension}"
                if not os.path.isfile(new_path):
                    file_path = new_path
                    break
                else:
                    accum += 1

        return file_path
    

    def download_json(self) -> None:
        """
        Creates a .json file of this downloader's data

        Raises:
            ValueError: if the file cannot be written to due to invalid file extension
        """
        if self.file_path.endswith(".json"):
            df = pd.DataFrame(self.data_dict)
            df.to_json(self.file_path)
        else:
            raise ValueError("File path must end in .json to download json file")
        

    def download_md(self) -> None:
        """
        Creates a .md (markdown) file of this downloader's data

        Raises:
            ValueError: if the file cannot be written to due to invalid file extension
        """
        if self.file_path.endswith(".md"):
            df = pd.DataFrame(self.data_dict)
            df.to_markdown(self.file_path)
        else:
            raise ValueError("File path must end in .md to download md file")
        

    def download_csv(self) -> None:
        """
        Creates a .csv file of this downloader's data

        Raises:
            ValueError: if the file cannot be written to due to invalid file extension
        """
        if self.file_path.endswith(".csv"):
            df = pd.DataFrame(self.data_dict)
            df.to_csv(self.file_path)
        else:
            raise ValueError("File path must end in .csv to download csv file")
        

    def download_excel(self) -> None:
        """
        Creates a .xlsx file of this downloader's data

        Raises:
            ValueError: if the file cannot be written to due to invalid file extension
        """
        if self.file_path.endswith(".xlsx"):
            df = pd.DataFrame(self.data_dict)
            df.to_excel(self.file_path)
        else:
            raise ValueError("File path must end in .xlsx to download excel file")



