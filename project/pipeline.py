import os
import requests
import pandas as pd
from zipfile import ZipFile

# Ensure the data directory exists
data_dir = "/data"
os.makedirs(data_dir, exist_ok=True)

# URLs for the datasets
carbon_majors_url = "https://carbonmajors.org/evoke/391/get_cm_file?type=Basic&file=emissions_high_granularity.csv"
gdp_url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv"

def download_file(url, save_path):
    """Downloads a file from a URL and saves it to the specified path."""
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {save_path}")

def extract_zip(file_path, extract_to):
    """Extracts a zip file to the specified directory."""
    with ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {file_path} to {extract_to}")

def transform_carbon_majors(data_path):
    """Transforms the Carbon Majors dataset."""
    df = pd.read_csv(data_path)
    df = df[['Entity', 'Year', 'Total Emissions (MtCO2e)']]
    return df

def transform_gdp(data_path):
    """Transforms the GDP dataset."""
    df = pd.read_csv(data_path, skiprows=4)
    df = df[['Country Name', 'Country Code', 'Indicator Name'] + [str(year) for year in range(2000, 2023)]]
    return df

def save_dataframe_to_csv(df, save_path):
    """Saves a pandas DataFrame to a CSV file."""
    df.to_csv(save_path, index=False)
    print(f"Saved DataFrame to {save_path}")

def main():
    # Download datasets
    carbon_majors_path = os.path.join(data_dir, "emissions_high_granularity.csv")
    gdp_path = os.path.join(data_dir, "world_bank_gdp.zip")
    
    download_file(carbon_majors_url, carbon_majors_path)
    download_file(gdp_url, gdp_path)
    
    # Extract GDP dataset
    extract_zip(gdp_path, data_dir)
    
    # Transform datasets
    carbon_majors_df = transform_carbon_majors(carbon_majors_path)
    gdp_df = transform_gdp(os.path.join(data_dir, "API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4902591.csv"))
    
    # Save transformed data to CSV
    save_dataframe_to_csv(carbon_majors_df, os.path.join(data_dir, "carbon_majors_processed.csv"))
    save_dataframe_to_csv(gdp_df, os.path.join(data_dir, "world_bank_gdp_processed.csv"))

if __name__ == "__main__":
    main()
