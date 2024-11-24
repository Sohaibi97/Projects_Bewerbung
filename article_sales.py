import pandas as pd
import os

def get_monthly_sales(x): # x here is the article number as a number
    # here is the path i am using saved in a variable
    path = "data\\Absätze.xlsx"
    # test the path and download the data
    if not os.path.exists(path):
        raise FileNotFoundError(f"Die Datei '{path}' wurde nicht gefunden.")
    # download the data now
    data = pd.read_excel(path)

    # i convert both Artikelnummer in DataFrame and input x to a string and locate the article number in the
    # data frame
    article_row = data.loc[data['Artikelnummer'].astype(str) == str(x)]

    # now i retrieve the value of AbsatzMonatlich if the article number exists
    if not article_row.empty:
        article_sale = article_row['AbsatzMonatlich'].iloc[0]
        return article_sale
    else: # if not i just print that it doesnt exist
        print(f"Article {x} not found.") # just print so the program doesnt stop
        return None
