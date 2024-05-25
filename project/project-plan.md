# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing the Relationship between Renewable Energy Adoption, CO2 Emissions, and Economic Growth in Germany, Norway, and Bulgaria (2000–2021)

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How does GDP correlates with the Energy Consumption/demand and CO2 Emissions from 2000-2021?
2. How has adoption of renewable energy sources (total energy generation, renewable energy generation, share of generation) impacted CO2 emissions in Germany, Norway, and Bulgaria from 2000 to 2021?
3. What is the correlation between energy demand and renewable energy generation in those countries?
4. Which renewable energy (e.g. hydro, solar, wind, bio) mostly used in Germany, Norway, and bulgaria? how do they correlate with the CO2 Emissions there?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to analyze the relationship between economic growth (GDP per capita), energy consumption, renewable energy adoption, and CO2 emissions in Germany, Norway, and Bulgaria from 2000 to 2021. By utilizing datasets that include CO2 emissions, energy demand/consumption, renewable energy generation, and GDP, the study will explore how economic development influences energy consumption and emissions. Additionally, it will assess the impact of renewable energy adoption on reducing CO2 emissions and meeting energy demands. Germany, Norway, and Bulgaria were chosen to represent countries in Europe with different GDP levels, providing a diverse perspective on the effects of renewable energy policies. The findings will provide insights into the effectiveness of renewable energy policies and the role of economic growth in climate change mitigation efforts.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: European Electricity Dataset
* Metadata URL: https://ember-climate.org/insights/research/european-electricity-review-2022/#supporting-material
* Data URL: https://ember-climate.org/app/uploads/2022/02/EER_2022_raw_data.zip
* Data Type: CSV
* Description: This dataset contains yearly electricity generation, emissions, and demand data for over 200 geographies. Data is collected from multi-country datasets (EIA, Eurostat, BP, UN) as well as national sources (e.g China data from the National Bureau of Statistics). For this project, we focus on the datasets for the period of 2000-2021 and specific chosen countries in europe.

### Datasource2: World GDP Dataset
* Metadata URL: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=NY.GDP.MKTP.CD
* Data URL: https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv
* Data Type: CSV
* Description: Country GDP in US dollars for the period of 1960 to 2021. For this project, we focus on the datasets for the period of 2000-2021 and specific chosen countries in europe. 

### Datasource3: Global Renewable Power Sectors Target 2030
* Metadata URL: https://ember-climate.org/data-catalogue/global-renewable-targets-2030-power/
* Data URL: https://ember-climate.org/app/uploads/2024/01/targets_download_240111.xlsx
* Data Type: CSV
* Description: latest data on national targets for renewable power in 2030 from 57 countries and the EU. For this project we focus on specific chosen countries in europe.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Problem Statement and Data Collection [#1][i1]
2. Data cleaning and preprocessing [#2][i2]
3. Data report [#3][i3]
3. Data analysis, interpretation and visualization [#4][i4]
4. Final Report [#5][i5]

[i1]: https://github.com/Jovinjo/made-rep/issues/1
[i2]: https://github.com/Jovinjo/made-rep/issues/2
[i3]: https://github.com/Jovinjo/made-rep/issues/3
[i4]: https://github.com/Jovinjo/made-rep/issues/4
[i5]: https://github.com/Jovinjo/made-rep/issues/5


