import tkinter as tk
from new_column_view import start_graph # Import the function that starts the graph
from article_sales_view import choose_article # Import the function to choose an article

def launch_table():
    start_graph()

def launch_article():
    choose_article()

def main():
    root = tk.Tk()
    root.title("Choose Your Option")

    # Screen positioning
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 600
    height = 200
    x_coordinate = (screen_width/2) - (width/2)
    y_coordinate = (screen_height/2) - (height/2)
    root.geometry(f'{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}')

    label = tk.Label(root, text="Do you want to view the table or just one article?")
    label.pack(pady=10)

    button_table = tk.Button(root, text="View Table", command=launch_table)
    button_table.pack(pady=5)

    button_article = tk.Button(root, text="Choose Article", command=launch_article)
    button_article.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
    