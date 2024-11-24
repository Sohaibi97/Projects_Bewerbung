import tkinter as tk
from article_sales import get_monthly_sales 

# this function is used when the user give the article number and click show sales
def display_sales(entry_widget, label_result):
    # saving the text value from the entry widget
    user_input = entry_widget.get()
    # checking if the input is empty or contains only spaces
    if not user_input.strip():
        label_result.config(text="Please enter a valid article number.")
        return

    try:
        # i try to convert the input to an integer
        article_number = int(user_input)
    except ValueError:
        # If conversion fails, it shows an error message
        label_result.config(text="Please enter a valid numeric article number.")
        return
    
    monthly_sales = get_monthly_sales(article_number) # iuse the function to get the results
    # now i give the results
    if monthly_sales is not None:
        label_result.config(text=f"The monthly Sales for the Article is {article_number}: {monthly_sales} items")
    else: # if the article isnt found
        label_result.config(text=f"Article {article_number} try with a valid article number.") 

def choose_article():
    root = tk.Tk() # i am creating the article sales main view
    root.title("Article Sales Viewer")

    # Screen positioning
    # taking the info from the user screen
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()
    # the size of the interface
    width = 600
    height = 400
    #the coordination for the center
    x_coordinate = (screen_width/2) - (width/2)
    y_coordinate = (screen_height/2) - (height/2)
    # the position in regard to the screem user
    root.geometry(f'{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}')

    # add a frame
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20) #once more just to make it visually more appealing

    label = tk.Label(frame, text="Enter the Article Number:") # the text shown to the user
    label.grid(row=0, column=0) # its position

    entry_widget = tk.Entry(frame) # the field where the user writes the article number
    entry_widget.grid(row=0, column=1) # its position

    label_result = tk.Label(frame, text="") #the answer will be here
    label_result.grid(row=2, column=0, columnspan=2) # the position of the answer

    # create the buttom for running the function and calling display_sales
    button_calculate = tk.Button(frame, text="Show Sales", command=lambda: display_sales(entry_widget, label_result))
    button_calculate.grid(row=1, column=0, columnspan=2) # the position of the buttom

    root.mainloop() #keep the function running
#choose_article()
