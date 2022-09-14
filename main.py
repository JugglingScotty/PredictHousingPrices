# Ensure the following files are available in the folder containing this document.
# MORTGAGE30US.csv, RRVRUSQ156N.csv, data/CPIAUCSL.csv

# Import pandas for use with parsing the data
import pandas as pd
from datetime import timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Create a list of the cvs files to be used by the py script.  about Economic conditions in the US.
    fed_files = ["data/MORTGAGE30US.csv", "data/RRVRUSQ156N.csv", "data/CPIAUCSL.csv"]
    # Median sale price of houses and their house value FROM Zillow
    zillow_files = ["data/Metro_median_sale_price_uc_sfrcondo_week.csv",
                    "data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_month.csv"]

    # Todo Create a single function to read in the fed and zillow files.

    # Read in the files as pandas dataframes
    dfs_fed = [pd.read_csv(f, parse_dates=True, index_col=0) for f in fed_files]
    dfs_zil = [pd.read_csv(f) for f in zillow_files]

    # Todo Customize the zillow data by picking your local region

    fed_data = pd.concat(dfs_fed, axis=1)

    # uses the Forward Fill command from pandas.  Assumes that the same rate is used each day for the upcoming
    # quarter/month.
    fed_data = fed_data.ffill()

    # reformat the data so it is consistent with federal reserve data
    dfs_zil = [pd.DataFrame(df.iloc[0, 5:]) for df in dfs_zil]

    for df in dfs_zil:
        df.index = pd.to_datetime(df.index)
        df["month"] = df.index.to_period("M")

    price_data = dfs_zil[0].merge(dfs_zil[1], on="month")
    price_data.index = dfs_zil[0].index

    del price_data["month"]
    price_data.columns = ["price", "value"]

    fed_data = fed_data.dropna()

    fed_data.index = fed_data.index + timedelta(days=2)

    price_data = fed_data.merge(price_data, left_index=True, right_index=True)

    price_data.columns = ["interest", "vacancy", "cpi", "price", "value"]

    print(price_data)

    # Todo Machine Learning - Target
    # Todo Machine Learning - Next Step
