import requests
import zipfile
import io
import pandas as pd
import os
from zipfile import ZipFile

def extract_gdp_data(gdp_url,csv_name):
    try: 
        # Send a GET request to the URL to download the carbon data
        response = requests.get(gdp_url)
        response.raise_for_status()
        print(f"Downloaded ZIP file")

        with ZipFile(io.BytesIO(response.content)) as zip_ref:
            # Get a list of all files in the zip archive
            zip_file_names = zip_ref.namelist()
            csv_files = [f for f in zip_file_names if os.path.basename(f) == csv_name]

            if not csv_files:
                print(f"No CSV file with the name '{csv_name}' found in the zip archieve")
                return None
            else: 
                with zip_ref.open(csv_name) as file:
                    df = pd.read_csv(file,encoding='ISO-8859-1',skiprows=4)
                    print(f"CSV file '{csv_name}' is loaded as dataframe successfully")
                    return df
    except requests.RequestException as e:
        print(f"ZIP file '{e}' failed to be downloaded")
        return None
    except zipfile.BadZipFile as e:
        print(f"ZIP File '{e}' failed to be read")
        return None
    
def extract_carbon_data(carbon_url,csv_name):
    try:
        # Send a GET request to the URL to download the carbon data
        response = requests.get(carbon_url)
        response.raise_for_status()  
        # Read the CSV content from the response and decode it as UTF-8
        df = pd.read_csv(io.StringIO(response.content.decode('utf-8')))
        print("CSV Data downloaded and loaded into DataFrame successfully.")
        return df
    except requests.RequestException as e:
        print(f"Failed to download carbon data: {e}")
        return None