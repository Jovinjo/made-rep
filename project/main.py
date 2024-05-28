from extraction import extract_zip_data
from transformation import transform_eer_data,transform_gdp_data
from saving import save_dataframe_to_csv

def main():
    try:
        # Extract, transform, and save EER (Demand, Emission, Generation) data
        eer_url = "https://ember-climate.org/app/uploads/2022/02/EER_2022_raw_data.zip"
        datasets = [
            {"csv_name": "EER_2022_emissions.csv", "df_type": "emission", "output_csv": "emission.csv"},
            {"csv_name": "EER_2022_country_overview.csv", "df_type": "demand", "output_csv": "demand.csv"},
            {"csv_name": "EER_2022_generation.csv", "df_type": "generation", "output_csv": "generation.csv"}
        ]
        for dataset in datasets:
            df_extracted = extract_zip_data(eer_url, dataset["csv_name"], use_regex=False, skiprows=None)
            if df_extracted is not None:
                final_df = transform_eer_data(df_extracted, dataset["df_type"])
                save_dataframe_to_csv(final_df, dataset["output_csv"])
            else:
                raise ValueError(f"Failed to extract {dataset['df_type']} data")
        
        # Extract, transform, and save GDP data
        gdp_url = "https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv"
        gdp_name_csv = r"^API_NY\.GDP\.MKTP\.CD_DS2_en_csv_v2_\d+\.csv$"
        gdp_df = extract_zip_data(gdp_url,gdp_name_csv,use_regex=True,skiprows=4)
        if gdp_df is not None:
            final_gdp_df = transform_gdp_data(gdp_df)
            save_dataframe_to_csv(final_gdp_df,"world_gdp.csv")
        else:
            raise ValueError("Failed to extract generation data")
        
    except Exception as e:
        print(f"An error occurred when running the main function: {e}")

if __name__ == "__main__":
    main()