#exec_dash.py

import pandas as pd
import os
import matplotlib.pyplot as plt
import operator
import matplotlib.ticker as ticker

input_file = input("Input file name: ")

file_path = "/Users/pauldougherty/Desktop/python/p2/data/" + input_file

if (os.path.isfile(file_path)):
    file_stats = pd.read_csv(file_path)

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

    print("-----------------------")
    print("MONTH: " + months[month] + " " + year)


    print("-----------------------")
    print("CRUNCHING THE DATA...")


    print("-----------------------")

    monthly_sales_string = str("${0:.2f}".format(file_stats["sales price"].sum()))
    print("TOTAL MONTHLY SALES: " + monthly_sales_string)


    print("-----------------------")
    print("TOP SELLING PRODUCTS:")

    products = list(file_stats["product"].unique())

    product_and_sales = []

    for a in products:
        total_sales = file_stats[file_stats["product"] == a]["sales price"].sum()
        product_and_sales.append({"product":a, "sales":total_sales})


    product_and_sales = sorted(product_and_sales, key=operator.itemgetter("sales"), reverse=True)

    x = 1

    while x < 6:

        number_to_print = "${0:.2f}".format(product_and_sales[x]["sales"])

        print("    " + str(x) + ") " + product_and_sales[x]["product"] + ": " + number_to_print)
        x = x + 1

    print("-----------------------")
    print("VISUALIZING THE DATA...")

    product_names = []
    product_sales = []

    for s in product_and_sales:
      product_names.append(s["product"])
      product_sales.append(s["sales"])


    ## https://github.com/s2t2/exec-dash-starter-py/commit/01b261ca30ee4c64d93c2146a1659ae2c9d445a5
    fig, ax = plt.subplots()
    usd_formatter = ticker.FormatStrFormatter('$%1.2f')
    ax.yaxis.set_major_formatter(usd_formatter)

    plt.bar(product_names, product_sales)
    plt.ylabel("Sales (USD)")
    plt.xlabel("Product")
    plt.title("Top-Selling Products (" + months[month] + " " + year + ")")



    plt.show()

else:
    print("Invalid filename. The program will exit now.")
