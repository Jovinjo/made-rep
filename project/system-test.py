import os
import pandas as pd
from main import main

# Copying production data as a testing environment. Data privacy is not a concern here.

def column_name_check(df, expected_columns):
    return list(df.columns) == expected_columns

def year_category_check(df, year_column):
    return df[year_column].between(2000, 2021).all()

def countries_category_check(df, column, countries_column):
    return df[column].isin(countries_column).all()

def check_emission_df(df):
    expected_columns = ['Country Name', 'Year', 'Emissions Intensity (gCO2/kWh)', 'Emissions (MTcO2e)']
    assert column_name_check(df, expected_columns), "Emission dataframe columns do not match"
    assert year_category_check(df, 'Year'), "Emission dataframe contains years outside of 2000-2021"
    assert countries_category_check(df, 'Country Name', ['Bulgaria','Germany','Sweden']), "Emissions dataframe contains countries other than Bulgaria, Germany, Sweden"

def check_generation_df(df):
    expected_columns = ['Country Name', 'Year', 'Fuel Code', 'Fuel Description', 'Electricity Generation (TWh)', 'Share of Generation (%)']
    assert column_name_check(df, expected_columns), "Generation dataframe columns do not match"
    assert year_category_check(df, 'Year'), "Generation dataframe contains years outside of 2000-2021"
    assert countries_category_check(df, 'Country Name', ['Bulgaria','Germany','Sweden']), "Generation dataframe contains countries other than Bulgaria, Germany, Sweden"

def check_demand_df(df):
    expected_columns = ['Country Name', 'Year', 'Electricity Demand (TWh)', 'Electricity Demand per Capita (MWh)']
    assert column_name_check(df, expected_columns), "Demand dataframe columns do not match"
    assert year_category_check(df, 'Year'), "Demand dataframe contains years outside of 2000-2021"
    assert countries_category_check(df, 'Country Name', ['Bulgaria','Germany','Sweden']), "Demand dataframe contains countries other than Bulgaria, Germany, Sweden"

def check_world_gdp_df(df):
    expected_columns = ['Country Name', 'Country Code', 'Year', 'GDP (US$)']
    assert column_name_check(df, expected_columns), "GDP dataframe columns do not match"
    assert year_category_check(df, 'Year'), "GDP dataframe contains years outside of 2000-2021"
    assert countries_category_check(df, 'Country Name', ['Bulgaria','Germany','Sweden']), "GDP dataframe contains countries other than Bulgaria, Germany, Sweden"
        
def load_csv(filepath):
    return pd.read_csv(filepath)

def system_test_pipeline():
    try:
        # Run the main function
        main()

        # Validate output files exists
        assert os.path.isfile("../data/emission.csv"),"Emission data does not exist"
        print("> Emission data exist")
        assert os.path.isfile("../data/demand.csv"),"Demand data does not exist"
        print("> Demand data exist")
        assert os.path.isfile("../data/generation.csv"),"Generation data does not exist"
        print("> Generation data exist")
        assert os.path.isfile("../data/world_gdp.csv"),"GDP data does not exist"
        print("> GDP data exist")

        emission_df = load_csv("../data/emission.csv")
        demand_df = load_csv("../data/demand.csv")
        generation_df = load_csv("../data/generation.csv")
        world_gdp_df = load_csv("../data/world_gdp.csv")

        print("Validate each dataframes....")
        check_emission_df(emission_df)
        check_demand_df(demand_df)
        check_generation_df(generation_df)
        check_world_gdp_df(world_gdp_df)

        print("System test passed: all dataframes are validated")
    except Exception as e:
        print(f"System test failed: {e}")
        raise

if __name__ == "__main__":
    system_test_pipeline()
