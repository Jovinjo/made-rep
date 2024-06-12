import os
import pandas as pd
from io import StringIO
from transformation import transform_eer_data,transform_gdp_data
from saving import save_dataframe_to_csv

# Using mock data as testing environment, including various years and countries.

mock_emission_data = StringIO("""\
country_name,country_code,year,emissions_intensity_gco2_kwh,emissions_mtc02e
Austria,AUT,2019,92,7
Bulgaria,BGR,2000,485,20
Germany,DEU,2000,558,322
Germany,DEU,1997,520,334
Sweden,SWE,2008,17,3""")

mock_generation_data = StringIO("""\
country_name,country_code,eu_member,year,fuel_code,fuel_desc,generation_twh,share_of_generation_pct,yoy_abs_change,yoy_pct_change
Austria,AUT,1,2019,GAS,Gas,8.87,15.86,0.4,4.72
Bulgaria,BGR,1,2000,OTHFOSS,Other Fossil,0.79,1.8,-0.26,-24.76
Germany,DEU,1,1997,WIND,Wind,5.53,1.0,0.94,20.48
Germany,DEU,1,2000,BIO,Bioenergy,4.33,0.76,0.82,23.36
Sweden,SWE,1,2008,BIO,Bioenergy,3.78,2.34,-0.32,-7.8""")

mock_demand_data = StringIO("""\
country_name,country_code,eu_member,year,generation_twh,net_import_twh,demand_twh,demand_mwh_per_capita
Austria,AUT,1,2019,59.92,-1.9,58.02,7.206
Bulgaria,BGR,1,2000,46.55,-7.81,38.74,5.494
Germany,DEU,1,1997,581.4,-18.99,562.41,6.713
Germany,DEU,1,2000,548.01,-2.35,545.66,6.704
Sweden,SWE,1,2008,145.23,4.68,149.91,16.879""")

mock_world_gdp_data = StringIO("""\
Country Name,Country Code,Indicator Name,Indicator Code,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023
Bulgaria,BGR,GDP (current US$),NY.GDP.MKTP.CD,101234567,109876543,115432109,120987654,126543210,132098765,137654321,143209876,148765432,154320987,159876543,165432109,170987654,176543210,182098765,187654321,193209876,198765432,204320987,209876543,215432109,220987654,226543210,232098765,237654321,243209876,248765432,254320987,259876543,265432109,270987654,276543210,282098765,287654321,293209876,298765432,304320987,309876543,315432109,320987654,326543210,332098765,337654321,343209876,348765432,354320987,359876543,365432109,370987654,376543210,382098765,387654321,393209876,398765432,404320987,409876543,415432109,420987654,426543210,420987654,619012345,382098765,598901234,365432109
Bangladesh,BGD,GDP (current US$),NY.GDP.MKTP.CD,123456789,132456789,141234567,150123456,159012345,168901234,178901234,189012345,198901234,209012345,218901234,229012345,239012345,248901234,259012345,268901234,279012345,289012345,298901234,309012345,319012345,328901234,339012345,349012345,358901234,369012345,379012345,388901234,399012345,409012345,418901234,429012345,439012345,448901234,459012345,469012345,478901234,489012345,499012345,508901234,519012345,529012345,538901234,549012345,559012345,568901234,579012345,589012345,598901234,609012345,619012345,628901234,639012345,649012345,658901234,669012345,679012345,688901234,699012345,709012345,649012345,658901234,639012345,609012345
Germany,DEU,GDP (current US$),NY.GDP.MKTP.CD,987654321,1098765432,1210987654,1320987654,1432098765,1543209877,1654320988,1765432109,1876543210,1987654321,2098765432,2209876543,2310987654,2420987654,2532098765,2643209877,2754320988,2865432109,2976543210,3087654321,3198765432,3309876543,3420987654,3532098765,3643209877,3754320988,3865432109,3976543210,4087654321,4198765432,4309876543,4420987654,4532098765,4643209877,4754320988,4865432109,4976543210,5087654321,5198765432,5309876543,5420987654,5532098765,5643209877,5754320988,5865432109,5976543210,6087654321,6198765432,6309876543,6420987654,6532098765,6643209877,6754320988,6865432109,6976543210,7087654321,7198765432,6420987654,1990123456,2012345678,619012345,598901234,6420987654,6532098765
Sweden,SWE,GDP (current US$),NY.GDP.MKTP.CD,876543210,901234567,923456789,945678901,967890123,990123456,1012345679,1034567890,1056789012,1078901234,1101234567,1123456789,1145678901,1167890123,1190123456,1212345678,1234567890,1256789012,1278901234,1301234567,1323456789,1345678901,1367890123,1390123456,1412345678,1434567890,1456789012,1478901234,1501234567,1523456789,1545678901,1567890123,1590123456,1612345678,1634567890,1656789012,1678901234,1701234567,1723456789,1745678901,1767890123,1790123456,1812345678,1834567890,1856789012,1878901234,1901234567,1923456789,1945678901,1967890123,1990123456,2012345678,2034567890,2056789012,2078901234,2101234567,2123456789,2145678901,2167890123,2190123456,2212345678,1901234567,1945678901,1990123456""")


def column_name_check(df, expected_columns):
    return list(df.columns) == expected_columns

def year_category_check(df, year_column):
    return df[year_column].between(2000, 2021).all()

def countries_category_check(df, column, countries_column):
    return df[column].isin(countries_column).all()

def check_dataframe(df, expected_columns):
    assert column_name_check(df, expected_columns), f"Dataframe columns do not match: {expected_columns}"
    assert year_category_check(df, 'Year'), f"Dataframe contains years outside of 2000-2021"
    assert countries_category_check(df, 'Country Name', countries_column=['Bulgaria', 'Germany', 'Sweden']), f"Dataframe contains countries other than Bulgaria,Germany,Sweden"
        
def load_csv(filepath):
    return pd.read_csv(filepath)

def test_data_pipeline():

    data_sources = [
        {"name": "emission", "data": mock_emission_data, "expected_columns": ['Country Name', 'Year', 'Emissions Intensity (gCO2/kWh)', 'Emissions (MTcO2e)']},
        {"name": "generation", "data": mock_generation_data, "expected_columns": ['Country Name', 'Year', 'Fuel Code', 'Fuel Description', 'Electricity Generation (TWh)', 'Share of Generation (%)']},
        {"name": "demand", "data": mock_demand_data, "expected_columns": ['Country Name', 'Year', 'Electricity Demand (TWh)', 'Electricity Demand per Capita (MWh)']},
        {"name": "world_gdp", "data": mock_world_gdp_data, "expected_columns": ['Country Name', 'Country Code', 'Year', 'GDP (US$)']}
    ]

    try:
        for source in data_sources:
            # transform data
            if source['name'] in ["emission", "generation", "demand"]:
                df = transform_eer_data(load_csv(source['data']), source['name'])
            else:
                df = transform_gdp_data(load_csv(source['data']))
            
            # save dataframe to csv
            save_dataframe_to_csv(df, f"{source['name']}.csv")
            assert os.path.isfile(f"../data/{source['name']}.csv"), f"{source['name']} data does not exist"
            
            # Validate dataframe and make sure output file exist
            print(f"Check if {source['name']}.csv exist")
            check_dataframe(df, source['expected_columns'])
        
        print("System test passed: all dataframes are validated")
        
    except Exception as e:
        print(f"System test failed: {e}")
        raise

if __name__ == "__main__":
    test_data_pipeline()
