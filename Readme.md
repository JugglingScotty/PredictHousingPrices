Going to try to create a Housing Prices app in Python.  It will:

Forecast house prices using Python and Machine Learning
1. Get economic housing data from the federal reserve.  
2. Combine it with house price data from Zillow.  
3. Train a random forest classifier to predict

Will measure model accuracy.  

You'll need to download a few csv files to run this project. They are in this directory.

If you want to get newer versions:

    Federal reserve data
        [CPI dataset](https://fred.stlouisfed.org/series/CPIAUCSL) - CPIAUCSL.csv
        [Rental vacancy rate](https://fred.stlouisfed.org/series/RRVRUSQ156N) - RRVRUSQ156N.csv
        [Mortgage interest rates](https://fred.stlouisfed.org/series/MORTGAGE30US) - MORTGAGE30US.csv
    [Zillow data](https://www.zillow.com/research/data/)
        ZHVI (raw, weekly) - Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv
        Median sale price (raw, all homes, weekly) - Metro_median_sale_price_uc_sfrcondo_week.csv


Next Steps to improve the model:
* Continue to improve it.  