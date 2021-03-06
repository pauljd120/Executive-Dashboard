from exec_dash import to_usd, get_top_sellers

import pandas as pd
import os
import matplotlib.pyplot as plt
import operator
import matplotlib.ticker as ticker

def test_to_usd():
    result = to_usd(50)
    assert result == "$50.00"

def test_get_top_sellers():
    file_name = "201711.csv"

    file_path = os.path.join("data/", file_name)

    file_stats = pd.read_csv(file_path)

    month = int(file_name[5:6])
    year = file_name[:4]

    product_and_sales = []

    result = get_top_sellers(file_stats, product_and_sales)

    assert str(result[0]) == "{'product': 'Button-Down Shirt', 'sales': 5399.15}"
    
    
    
    
    
