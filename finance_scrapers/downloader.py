import pandas as pd

class Downloader:
    """Represents a tool for downloading a dictionary of data to a file."""

    @staticmethod
    def __transpose_and_fill(df: pd.DataFrame) -> pd.DataFrame:
        """
        Transposes the given dataframe and fills its empty spaces with 'N/A'

        Args:
            df: the dataframe to transpose and fill

        Returns:
            The updated dataframe
        """
        updated_df = df.transpose()
        updated_df.fillna("", inplace=True)
        return updated_df
    
    @staticmethod
    def download_json(data: dict, file_path: str) -> None:
        """
        Creates a .json file of this downloader's data
        """
        df = pd.DataFrame(data)
        df.fillna("", inplace=True)
        df.to_json(file_path, indent=4)
        
    @staticmethod
    def download_md(data: dict, file_path: str) -> None:
        """
        Creates a .md (markdown) file of this downloader's data
        """
        df = pd.DataFrame(data)
        updated_df = Downloader.__transpose_and_fill(df)
        updated_df.to_markdown(file_path)
        
    @staticmethod
    def download_csv(data: dict, file_path: str) -> None:
        """
        Creates a .csv file of this downloader's data
        """
        df = pd.DataFrame(data)
        updated_df = Downloader.__transpose_and_fill(df)
        updated_df.to_csv(file_path)
        
    @staticmethod
    def download_excel(data: dict, file_path: str) -> None:
        """
        Creates a .xlsx file of this downloader's data
        """
        df = pd.DataFrame(data)
        updated_df = Downloader.__transpose_and_fill(df)
        updated_df.to_excel(file_path)



