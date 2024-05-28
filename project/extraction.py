import requests
import zipfile
import io
import pandas as pd
import os
import re
from zipfile import ZipFile

# Extract eer datasets
def extract_zip_data(target_url,csv_name,use_regex=False,skiprows=None):
    try: 
        # Send a GET request to the URL to download the carbon data
        response = requests.get(target_url)
        response.raise_for_status()
        print(f"Downloaded ZIP file")

        with ZipFile(io.BytesIO(response.content)) as zip_ref:
            # Get a list of all files in the zip archive
            zip_file_names = zip_ref.namelist()
            if use_regex:
                csv_files = [f for f in zip_file_names if re.match(csv_name, os.path.basename(f))]
            else:
                csv_files = [f for f in zip_file_names if os.path.basename(f) == csv_name]

            if not csv_files:
                print(f"No CSV file '{csv_files[0]}' found in the zip archieve")
                return None
            else: 
                with zip_ref.open(csv_files[0]) as file:
                    if skiprows is not None:
                        df = pd.read_csv(file, encoding='ISO-8859-1', skiprows=skiprows)
                    else:
                        df = pd.read_csv(file, encoding='ISO-8859-1')
                    print(f"CSV file '{csv_files[0]}' is loaded as dataframe successfully")
                    return df
    except requests.RequestException as e:
        ValueError(f"ZIP file '{e}' failed to be downloaded")
        return None
    except zipfile.BadZipFile as e:
        ValueError(f"ZIP File '{e}' failed to be read")
        return None

# def extract_xlsx_data(target_url,sheet_name):
#     try:
#         # Send a GET request to the URL to download the Excel file
#         response = requests.get(target_url)
#         response.raise_for_status()  # Raise an HTTPError on a bad status
#         print("Excel file downloaded successfully.")
    
#         # Read the Excel content from the response
#         df = pd.read_excel(io.BytesIO(response.content), sheet_name=sheet_name)
#         print("Excel data loaded into DataFrame successfully.")
#         return df
#     except requests.RequestException as e:
#         print(f"Failed to download Excel file: {e}")
#         return None
#     except ValueError as e:
#         print(f"Failed to load Excel data into DataFrame: {e}")
#         return None


