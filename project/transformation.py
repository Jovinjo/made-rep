import pandas as pd

def transform_eer_data(eer_df,df_type):
    try:
        #filter for specific countries (Germany, Sweden, Bulgaria)
        filtered_country_df = eer_df[eer_df['country_name'].isin(['Germany','Sweden','Bulgaria'])]
        #filter for the year range 2000-2021
        filtered_year_df = filtered_country_df[(filtered_country_df['year'] >= 2000) & (filtered_country_df['year'] <= 2021)]
        

        # Drop columns based on dataframe type
        if df_type == 'demand':
            columns_to_drop = ['country_code','eu_member', 'generation_twh', 'net_import_twh']
        elif df_type == 'emission':
            columns_to_drop = ['country_code']
        elif df_type == 'generation':
            columns_to_drop = ['country_code','eu_member', 'yoy_abs_change', 'yoy_pct_change']
            # Filter the fuel codes (focus on renewable energies)
            filtered_year_df = filtered_year_df[filtered_year_df['fuel_code'].isin(['BIO', 'HYDRO', 'SOLAR', 'WIND', 'OTHRENEW'])]
        else:
            raise ValueError("Unknown dataframe")
        final_eer_df = filtered_year_df.drop(columns=columns_to_drop)


        # Rename columns
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
        renamed_df = final_eer_df.rename(columns=column_rename_dict)

        return renamed_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
    
def transform_gdp_data(gdp_df):
    try:
        #filter for specific countries (Germany, Sweden, Bulgaria)
        filtered_country_df = gdp_df[gdp_df['Country Name'].isin(['Germany','Sweden','Bulgaria'])]
        
        # Drop unnecessary columns
        columns_to_drop = ['Indicator Code','Indicator Name','2022','2023','Unnamed: 68'] + [str(year) for year in range(1960, 2000)]

        filtered_columns_df = filtered_country_df.drop(columns=columns_to_drop)

        id_vars = ['Country Name', 'Country Code']
        final_gdp_df = pd.melt(filtered_columns_df, id_vars=id_vars, var_name='Year', value_name='GDP (US$)')

        # Convert the 'Value' column to numeric, errors='coerce' will turn non-convertible values into NaN
        final_gdp_df['GDP (US$)'] = pd.to_numeric(final_gdp_df['GDP (US$)'], errors='coerce')

        # Now, divide by 1e9 to convert to billions
        # final_gdp_df['GDP (Billion US$)'] = final_gdp_df['GDP (Billion US$)'] / 1e9

        return final_gdp_df
    
    except Exception as e:
        print(f"Error in transforming data: {e}")
        return None
