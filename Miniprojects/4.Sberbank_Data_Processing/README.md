### Sberbank Data Analytics with Pandas

Dataset from [Kaggle Competition: Sberbank Russian Housing Market](https://www.kaggle.com/c/sberbank-russian-housing-market). This notebook contains the most essential and useful techniques for data analysis in solving a real-world problem with key Python data analysis libraries: pandas and numpy. We’ll go through data loading and data frame creation, selection and query, grouping and function applying, plotting and writing data to file.



**Data Description**

The aim of this competition is to predict the sale price of each property. The target variable is called **price_doc** in train.csv.

The training data is from August 2011 to June 2015, and the test set is from July 2015 to May 2016. The dataset also includes information about overall conditions in Russia's economy and finance sector, so you can focus on generating accurate price forecasts for individual properties, without needing to second-guess what the business cycle will do.

- **train.csv, test.csv:** information about individual transactions. The rows are indexed by the "id" field, which refers to individual transactions (particular properties might appear more than once, in separate transactions). These files also include supplementary information about the local area of each property.

