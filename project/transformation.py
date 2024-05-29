import pandas as pd

def transform_eer_data(eer_df,df_type):
    try:
        # Filter for specific countries (Germany, Sweden, Bulgaria) and filter for the year range 2000-2021
        filtered_country_df = eer_df[eer_df['country_name'].isin(['Germany','Sweden','Bulgaria'])]
        filtered_year_df = filtered_country_df[(filtered_country_df['year'] >= 2000) & (filtered_country_df['year'] <= 2021)]
        
        # Columns to drop based on dataframe type (demand, emission, generation)
        if df_type == 'demand':
            columns_to_drop = ['country_code','eu_member', 'generation_twh', 'net_import_twh']
        elif df_type == 'emission':
            columns_to_drop = ['country_code']
        elif df_type == 'generation':
            columns_to_drop = ['country_code','eu_member', 'yoy_abs_change', 'yoy_pct_change']
        else:
            raise ValueError("Unknown dataframe")
        
        # Drop the specified columns from the filtered dataframe
        final_df = filtered_year_df.drop(columns=columns_to_drop)

        # Dictionary for renaming columns to more readable names
        column_rename_dict = {
            'country_name': 'Country Name',
            'year': 'Year',
            'demand_twh': 'Electricity Demand (TWh)',
            'demand_mwh_per_capita': 'Electricity Demand per Capita (MWh)',
            'fuel_code': 'Fuel Code',
            'fuel_desc': 'Fuel Description',
            'generation_twh': 'Electricity Generation (TWh)',
            'share_of_generation_pct': 'Share of Generation (%)',
            'emissions_intensity_gco2_kwh': 'Emissions Intensity (gCO2/kWh)',
            'emissions_mtc02e': 'Emissions (MTcO2e)',
        }

        # Rename the columns in the datagrame using the dictionary and return the transformed dataframe
        renamed_final_df = final_df.rename(columns=column_rename_dict)
        return renamed_final_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
    
def transform_gdp_data(gdp_df):
    try:
        # Filter for specific countries (Germany, Sweden, Bulgaria)
        filtered_country_df = gdp_df[gdp_df['Country Name'].isin(['Germany','Sweden','Bulgaria'])]
        
        # Drop unnecessary columns
        columns_to_drop = ['Indicator Code','Indicator Name','2022','2023','Unnamed: 68'] + [str(year) for year in range(1960, 2000)]
        filtered_columns_df = filtered_country_df.drop(columns=columns_to_drop)

        # Define the columns that will be kept as identifier variables in the melting process (Wide to Long format)
        id_vars = ['Country Name', 'Country Code']

        # Convert the dataframe from wide format to long format, create new column 'Year'
        final_gdp_df = pd.melt(filtered_columns_df, id_vars=id_vars, var_name='Year', value_name='GDP (US$)')

        # Convert the 'GDP (US$)' column to numeric and return transformed dataframe
        final_gdp_df['GDP (US$)'] = pd.to_numeric(final_gdp_df['GDP (US$)'], errors='coerce')
        return final_gdp_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
