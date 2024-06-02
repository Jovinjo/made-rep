# Project Plan

## Title
<!-- Give your project a short title. -->
Analyzing the Relationship between Renewable Energy Adoption, CO2 Emissions, and Economic Growth in Germany, Sweden, and Bulgaria (2000–2021)

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
How have GDP and the adoption of renewable energy sources (total energy generation, renewable energy generation, share of generation) influenced energy consumption and CO2 emissions in Germany, Norway, and Bulgaria from 2000 to 2021?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to analyze the relationship between economic growth (GDP), energy consumption, renewable energy adoption, and CO2 emissions in Germany, Sweden, and Bulgaria from 2000 to 2021. By utilizing datasets, the study aims to elucidate how changes in GDP and the adoption of renewable energy sources influence energy consumption patterns and carbon emissions in these countries. Germany, Sweden, and Bulgaria were chosen to  represent a spectrum of economic development and renewable energy policies, offering a comprehensive view of the relationship between economic growth, renewable energy utilization, and environmental outcomes. The findings will provide valuable insights into the efficacy of renewable energy strategies in mitigating CO2 emissions while accommodating economic growth.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: European Electricity Dataset
* Metadata URL: https://ember-climate.org/insights/research/european-electricity-review-2022/#supporting-material
* Data URL: https://ember-climate.org/app/uploads/2022/02/EER_2022_raw_data.zip
* Data Type: CSV Directory
* Description: TThe European Electricity Dataset from Ember provides a collection of datasets related to electricity generation, CO2 emissions, net import and demand across various countries in Europe. For this project, we will remove the net import dataset and focus on the other variables (generation, CO2 emissions and demand) to analyze the adoption of renewable energy sources for Germany, Sweden, and Bulgaria from 2000 to 2021.

### Datasource2: World GDP Dataset
* Metadata URL: https://databank.worldbank.org/reports.aspx?source=2&type=metadata&series=NY.GDP.MKTP.CD
* Data URL: https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv
* Data Type: CSV
* Description: This dataset provides annual GDP figures in US dollars for countries worldwide from 1960 to 2021. For this project, we will focus the GDP data for Germany, Sweden, and Bulgaria from 2000 to 2021.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Define Problem Statement and Objectives[#1][i1]
2. Identify and Collect Data[#2][i2]
2. Data Preparation and Processing (ETL pipeline)[#3][i3]
3. Data Report (Preliminary)[#4][i4]
3. Data Analysis, Interpretation, and Visualization[#5][i5]
4. Final Report (Result)[#6][i6]

[i1]: https://github.com/Jovinjo/made-rep/issues/1
[i2]: https://github.com/Jovinjo/made-rep/issues/2
[i3]: https://github.com/Jovinjo/made-rep/issues/3
[i4]: https://github.com/Jovinjo/made-rep/issues/4
[i5]: https://github.com/Jovinjo/made-rep/issues/5
[i6]: https://github.com/Jovinjo/made-rep/issues/6


