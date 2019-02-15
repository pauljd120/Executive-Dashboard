#exec_dash.py

import pandas as pd
import os
import matplotlib.pyplot as plt
import operator
import matplotlib.ticker as ticker

# utility function to convert float or integer to usd-formatted string (for printing), adapted from:
#  + https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

input_file = input("Input file name: ")

#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
file_path = os.path.join("data/", input_file)

#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/os.md#file-operations
if (os.path.isfile(file_path)):

    #https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/csv.md
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

    #went over this method in office hours with you
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

    #learned this during the in class graph exercise
    plt.bar(product_names, product_sales)
    plt.ylabel("Sales (USD)")
    plt.xlabel("Product")
    plt.title("Top-Selling Products (" + months[month] + " " + year + ")")

    #https://github.com/s2t2/exec-dash-starter-py/commit/a4478c28c6ce0fb393aca52b0cd0845cfe6c0f7c
    for bar_index, bar_size in enumerate(product_sales):
        h = bar_size# - 2 # to the right of the bar's right edge
        w = bar_index# - .5 # below the bar's top edge
        bar_label = to_usd(bar_size)
        ax.text(w, h, bar_label, ha="center", va="bottom")


    plt.tight_layout()
    plt.show()

else:
    print("Invalid filename. The program will exit now.")
