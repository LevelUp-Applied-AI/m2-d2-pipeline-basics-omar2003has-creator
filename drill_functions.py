import pandas as pd

def clean_column(series):
    """Fill NaN values with the series median. Returns the cleaned Series.

    Args:
        series (pd.Series): A pandas Series that may contain NaN values.

    Returns:
        pd.Series: The Series with NaN values replaced by the median.
    """
    median_val = series.median()
    return series.fillna(median_val)


def compute_revenue(quantity, price):
    """Multiply quantity and price element-wise. Returns a revenue Series.

    Args:
        quantity (pd.Series): A Series of unit quantities.
        price (pd.Series): A Series of unit prices.

    Returns:
        pd.Series: Element-wise product of quantity and price.
    """
    return quantity * price