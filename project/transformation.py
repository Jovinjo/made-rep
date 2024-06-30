import pandas as pd

def transform_eer_data(eer_df,df_type):
    try:
        # Filter for specific countries (Germany, Sweden, Bulgaria) and filter for the year range 2000-2021
        filtered_country_df = eer_df[eer_df['country_name'].isin(['Germany','Sweden','Bulgaria'])]
        filtered_year_df = filtered_country_df[(filtered_country_df['year'] >= 2000) & (filtered_country_df['year'] <= 2021)]
        
        # Columns to drop based on dataframe type (demand, emission, generation)
        if df_type == 'demand':
            columns_to_drop = ['country_code','eu_member','generation_twh','net_import_twh']
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

        # Set the correct data types for each column
        dtype_dict = {
            'Country Name': 'str',
            'Year': 'int64',
            'Electricity Demand (TWh)': 'float64',
            'Electricity Demand per Capita (MWh)': 'float64',
            'Fuel Code': 'str',
            'Fuel Description': 'str',
            'Electricity Generation (TWh)': 'float64',
            'Share of Generation (%)': 'float64',
            'Emissions Intensity (gCO2/kWh)': 'float64',
            'Emissions (MTcO2e)': 'float64',
        }
        
        for column, dtype in dtype_dict.items():
            if column in renamed_final_df.columns:
                renamed_final_df[column] = renamed_final_df[column].astype(dtype)
                
        return renamed_final_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
    
def transform_gdp_data(gdp_df):
    try:
        # Filter for specific countries (Germany, Sweden, Bulgaria)
        filtered_country_df = gdp_df[gdp_df['Country Name'].isin(['Germany','Sweden','Bulgaria'])]
        
        # Drop unnecessary columns
        columns_to_drop = ['Indicator Code','Indicator Name','2022','2023'] + [str(year) for year in range(1960, 2000)]
        filtered_columns_df = filtered_country_df.drop(columns=columns_to_drop)

        # Define the columns that will be kept as identifier variables in the melting process (Wide to Long format)
        id_vars = ['Country Name', 'Country Code']

        # Convert the dataframe from wide format to long format, create new column 'Year'
        final_gdp_df = pd.melt(filtered_columns_df, id_vars=id_vars, var_name='Year', value_name='GDP (US$)')

        # Convert 'Year' and 'GDP' to numeric, errors='coerce' will turn non-convertible values into NaN
        final_gdp_df['Year'] = pd.to_numeric(final_gdp_df['Year'], errors = 'coerce').astype('Int64')
        final_gdp_df['GDP (US$)'] = pd.to_numeric(final_gdp_df['GDP (US$)'], errors='coerce')

        # Drop rows where 'Year' and 'GDP' is NaN
        final_gdp_df.dropna(subset=['Year', 'GDP (US$)'], inplace=True) 

        # Now, divide by 1e9 to convert to billions for better understanding
        final_gdp_df['GDP (US$)'] = final_gdp_df['GDP (US$)'] / 1e9
        final_gdp_df.rename(columns={'GDP (US$)': 'GDP (Billion US$)'}, inplace=True)

        return final_gdp_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
