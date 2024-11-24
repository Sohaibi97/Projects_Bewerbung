import pandas as pd
import os
from adjust_excel import adjust_columns
from group_by_article import group_by_article

def calculate_sales_monthly(x): # x is the number of months we are comparing here
    # here is the path i am using saved in a variable
    path = "data\\Absätze.xlsx"
     # test the path and download the data
    if not os.path.exists(path):
        raise FileNotFoundError(f"Die Datei '{path}' wurde nicht gefunden.")
    # download the data now
    data = pd.read_excel(path)

    # group by article so we have the right results
    group_by_article(path)

    # creating the new column with the profits we made in average each month
    data['AbsatzMonatlich'] = (data['Absatz'] / x).round(2)

    # we save now the new column
    resultTable=data.to_excel("data\\Absätze.xlsx", index=False)
    adjust_columns("data\\Absätze.xlsx")
    
    return resultTable
