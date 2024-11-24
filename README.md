# README for Sales Calculation Tool

This tool is a GUI-based Python application to manage and analyze article sales data. It includes features to calculate monthly sales, group articles, and adjust Excel files for better readability. Below is a detailed guide:

---

## Description

The tool calculates and displays the monthly sales of articles based on user inputs. It offers two main functionalities:

1. **View Monthly Sales for All Articles**: Process a sales file and calculate average monthly sales for all articles.
2. **Check Sales of a Specific Article**: Look up and display the monthly sales for a specific article.

---

## Usage Instructions

### Prepare Your File:
- Download the "Umsätze" file from Weclapp under **"Berichtswesen -> Umsatz nach Artikel."**
- Save it as `Absätze.xlsx` in the `data` folder.

### Run the Main Application:
- Execute `main.py`.
- You will see two options:
  - **View Table**: Process and calculate monthly sales for all articles.
  - **Choose Article**: Look up sales for a specific article.

---

## Functionalities

### 1. View Monthly Sales for All Articles
- **Action**: Click **"View Table"**.
- **Details**:
  - You will be asked to input the number of months to calculate average sales.
  - The tool groups articles, adds a new column for monthly sales (`AbsatzMonatlich`), and adjusts the Excel file for readability.
- **Output**: The processed Excel file (`Absätze.xlsx`) will be updated.

### 2. Check Sales of a Specific Article
- **Action**: Click **"Choose Article."**
- **Details**:
  - A new window allows you to input an article number.
  - It displays the monthly sales for the given article or a message if the article is not found.

---

## File Overview

### 1. `main.py`
- **Purpose**: Entry point of the application.
- **Description**:
  - Provides a menu with two options: "View Table" and "Choose Article."
  - Launches the respective views based on user selection.

### 2. `new_column.py`
- **Purpose**: Calculate average monthly sales for all articles.
- **Key Steps**:
  - Group articles by their first 5 digits using `group_by_article.py`.
  - Add a column (`AbsatzMonatlich`) for monthly sales.
  - Save and format the updated Excel file.

### 3. `new_column_view.py`
- **Purpose**: Create the GUI for viewing and processing the sales table.
- **Key Features**:
  - Input field to specify the number of months.
  - Button to calculate and update the table.
  - Message displayed upon successful processing.

### 4. `group_by_article.py`
- **Purpose**: Group the sales data by the first 5 digits of the article numbers.
- **Key Features**:
  - Sums up relevant columns (`Kosten`, `Marge`, `Absatz`, `Nettoumsatz`).
  - Outputs a grouped Excel file.

### 5. `adjust_excel.py`
- **Purpose**: Format the Excel file for readability.
- **Key Features**:
  - Adjusts column widths based on the longest cell value in each column.

### 6. `article_sales.py`
- **Purpose**: Retrieve monthly sales for a specific article.
- **Key Features**:
  - Searches for the article number in the Excel file.
  - Returns the monthly sales or a "not found" message.

### 7. `article_sales_view.py`
- **Purpose**: Create the GUI for viewing sales of a specific article.
- **Key Features**:
  - Input field to enter the article number.
  - Button to retrieve and display sales data.

---

## Requirements

### Python Packages:
- `pandas`: For data manipulation.
- `openpyxl`: For handling Excel files.
- `tkinter`: For creating the GUI.

### File Structure:
- Ensure `Absätze.xlsx` is in the `data` folder.

---

## Known Issues
- Ensure input files are correctly formatted. If not grouped by `Artikelnummer`, results may be incorrect.
- Handle invalid or missing article numbers gracefully in the "Choose Article" feature.

---

## Additional Usage via .BAT File

If you prefer, the application can also be launched directly using a `.bat` file located on the desktop.

### Steps to Use the `.BAT` File
1. **Ensure Configuration**:
   - Make sure the `.bat` file is correctly set up to point to the `main.py` script in your project directory.
2. **Double-Click the .BAT File**:
   - Simply double-click the `.bat` file on your desktop.
   - This will automatically launch the main application (`main.py`) without requiring manual navigation or command-line inputs.

### Advantages of the `.BAT` File
- **Convenience**: No need to open a terminal or navigate to the project directory.
- **Ease of Access**: Keep the `.bat` file on your desktop or any frequently used location for quick access.
