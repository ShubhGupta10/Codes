import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector

def insert_pdf(file_name, file_data):
    """Insert a PDF into the database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Notebook',
            user='root',
            password='tiger'
        )
        cursor = connection.cursor()

        sql_insert_blob_query = """INSERT INTO pdf_files (name, file) VALUES (%s,%s)"""
        cursor.execute(sql_insert_blob_query, (file_name, file_data))
        
        connection.commit()
        messagebox.showinfo("Success", "PDF file inserted successfully as BLOB into pdf_files table")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert BLOB data into MySQL table {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def browse_file():
    """Open a file dialog to select a PDF file."""
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def submit_file():
    """Submit the selected PDF file to the database."""
    file_path = entry_file_path.get()
    if not file_path:
        messagebox.showwarning("Warning", "Please select a PDF file first")
        return

    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()
            file_name = file_path.split('/')[-1]
            insert_pdf(file_name, binary_data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")

# Set up the main application window
root = tk.Tk()
root.title("PDF File Upload")

# Create and place the widgets
label_file_path = tk.Label(root, text="PDF File Path:")
label_file_path.grid(row=0, column=0, padx=10, pady=10)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)

button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2, padx=10, pady=10)

button_submit = tk.Button(root, text="Submit", command=submit_file)
button_submit.grid(row=1, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
