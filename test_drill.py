"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    # Create a pd.Series with at least one NaN value
    # Using 1, 3, NaN, 5, 11 (Median of 1, 3, 5, 11 is 4.0)
    series = pd.Series([1, 3, np.nan, 5, 11])
    
    # Call clean_column() on it
    cleaned = clean_column(series)
    
    # Assert no NaN values remain in the result
    assert cleaned.isna().sum() == 0
    
    # Assert the NaN was filled with the correct median value (4.0)
    assert cleaned[2] == 4.0


def test_compute_revenue():
    # Create two small pd.Series (quantity and price)
    quantity = pd.Series([2, 5, 10])
    price = pd.Series([10.0, 2.0, 5.0])
    
    # Call compute_revenue() on them
    revenue = compute_revenue(quantity, price)
    
    # Assert the result matches the expected element-wise product
    expected = pd.Series([20.0, 10.0, 50.0])
    pd.testing.assert_series_equal(revenue, expected)