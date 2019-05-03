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
    
    assert result == "[{'product': 'Button-Down Shirt', 'sales': 5399.15}, {'product': 'Super Soft Hoodie', 'sales': 1950.0}, {'product': 'Khaki Pants', 'sales': 1869.0}, {'product': 'Super Soft Sweater', 'sales': 1349.91}, {'product': 'Vintage Logo Tee', 'sales': 669.9}, {'product': 'Sticker Pack', 'sales': 265.5}, {'product': 'Brown Boots', 'sales': 250.0}, {'product': 'Winter Hat', 'sales': 207.19999999999996}]"
    
    
    
    
    
