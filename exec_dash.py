#exec_dash.py

import pandas as pd
import os
import matplotlib.pyplot as plt

print("Input file name: ")

input_file = input()

file_path = "/Users/pauldougherty/Desktop/python/p2/data/" + input_file

if (os.path.isfile(file_path)):
    #file_stats = pd.read_csv(file_path)

    month = int(input_file[5:6])
    year = input_file[:4]

    months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }





    ##TEMP##
    my_list = [
        ["2018-09-01", "Super Soft Hoodie",	75.00, 3, 225.00],
        ["2018-09-01", "Vintage Logo Tee",	15.95, 5, 79.75],
        ["2018-09-02", "Super Soft Sweater", 149.99, 2, 299.98]
    ]
    df = pd.DataFrame(my_list)
    df.columns = ["date", "product", "unit price", "units sold", "sales price"]
    print("------")
    print(df.head(3))
    print("------")

    #BEST SELLING PRODUCTS
    #for index, row in df.iterrows():
    #    print(row["date"])





    #ACTUAL CODE
    print("-----------------------")
    print("MONTH: " + months[month] + " " + year)


    print("-----------------------")
    print("CRUNCHING THE DATA...")


    print("-----------------------")
    monthly_sales_string = str(df["sales price"].sum())
    print("TOTAL MONTHLY SALES: " + monthly_sales_string)


    print("-----------------------")
    print("TOP SELLING PRODUCTS:")
    print("  1) Button-Down Shirt: $6,960.35")
    print("  2) Super Soft Hoodie: $1,875.00")
    print("  3) etc.")
    ##figure out  a sorting method
    top_sellers = pd.DataFrame(
        {
            "product" : [],
            "sales volume" : []
        }

    )


    print("-----------------------")
    print("VISUALIZING THE DATA...")
    ##use matplotlib












else:
    print("Invalid filename. The program will exit now.")
