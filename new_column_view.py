import tkinter as tk
from new_column import calculate_sales_monthly

#This function is executed when the user clicks the "Calculate" button
def get_input_and_calculate(): #for the second interface after clicking view table
    x = float(entry_widget.get()) # here i get the user input (the number of the months we are comparing)
    calculate_sales_monthly(x)
    label_result.config(text="The calculation is done! Now go to the table in Data and see the excel table")
    if root.winfo_exists():  # we just check but we shouldnt actually because it always exists
        root.after(2000, root.destroy) # i give the user 3 seconds before closing the window

#This function sets up what we see inside the main window, like labels, the text box, and the button
def create_graph():
    global entry_widget # making entry_widget global so that it's accessible in other functions
    frame_graph = tk.Frame(root) # Frame is the container for all my widgets and buttoms and root is the interface
    frame_graph.pack(padx=20, pady=20) #adding extra space around the widget to make it visually appealing

    label = tk.Label(frame_graph, text="how many months are we looking at?") # add my question to Basile to the UI
    label.grid(row=0, column=0) # i define the position

    entry_widget = tk.Entry(frame_graph) # i create the widget for user input and put it on frame_graph
    entry_widget.grid(row=0, column=1) # the position of the widget

    # i create the buttom to start the calculation
    button_calculate = tk.Button(frame_graph, text="Calculate", command=get_input_and_calculate)
    button_calculate.grid(row=1, column=0, columnspan=2)

    # creating another widget to say the calculation is done
    global label_result
    label_result = tk.Label(frame_graph, text="")
    label_result.grid(row=2, column=0, columnspan=2)

# This function starts the entire program. It creates the main window where all the buttons,
# text boxes, and labels will appear.
def start_graph():
    global root # declaring root as golbal allows get_input_and_calculate to modify the window
    root = tk.Tk() # creates the main window
    root.title("Monthly Sales Calculation") # title of the window

    # the screen's width and height depends on the user screen info, therefore i get the information
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()

    # Setting the window's size
    width = 500
    height = 300

    # Ci calculate the position to center the window
    x_coordinate = (screen_width/2) - (width/2)
    y_coordinate = (screen_height/2) - (height/2)

    # i set the position of the window in regard of all the coordination i have
    root.geometry(f'{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}')

    create_graph() # i call the function to create the graph

    root.mainloop() # to keep the interaction running until the user close the interface
#start_graph()
