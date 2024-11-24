import pandas as pd

def group_by_article(path):
    # get the file
    data = pd.read_excel(path)

    # i just take the first 5 numbers of an article number because of the ebay articles
    data['Artikelnummer'] = data['Artikelnummer'].astype(str).str[:5]

    # i group now by article number so i get the sum of sales we made
    data = data.groupby('Artikelnummer').agg({
        'Kosten': 'sum',
        'Marge': 'sum',
        'Absatz': 'sum',
        'Nettoumsatz': 'sum'
    }).reset_index() # without restindex Artikelnummer becomes index

    # i save the modified dataFrame to a new excel file
    data.to_excel(path, index=False)
    return None
