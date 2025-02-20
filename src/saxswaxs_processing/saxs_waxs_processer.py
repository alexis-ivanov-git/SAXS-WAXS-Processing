import os
import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def process_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    total_list = []
    first_file_processed = False  
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".dat"):
            file_path = os.path.join(input_directory, filename)
            try:
                df = pd.read_csv(file_path, sep=r'\s+', header=None, engine='python')

                if df.shape[1] > 1:
                    total_list.extend(df.iloc[1:, 1].tolist())  
                    
                    if not first_file_processed:
                        output_filename = filename.replace(".dat", ".txt")
                        output_txt_path = os.path.join(output_directory, output_filename)
                        first_file_processed = True
                else:
                    print(f"Skipping {filename} (not enough columns).")

            except Exception as e:
                print(f"Error reading {filename}: {e}")

    if first_file_processed:
        with open(output_txt_path, 'w') as txt_file:
            for item in total_list:
                txt_file.write(f"{item}\n")

        messagebox.showinfo("Success", f"Data successfully exported to {output_txt_path}")
    else:
        messagebox.showerror("Error", "No valid .dat files were processed.")

def select_input_directory():
    directory = filedialog.askdirectory()
    input_dir_var.set(directory)

def select_output_directory():
    directory = filedialog.askdirectory()
    output_dir_var.set(directory)

def start_processing():
    input_dir = input_dir_var.get()
    output_dir = output_dir_var.get()
    
    if not input_dir or not output_dir:
        messagebox.showwarning("Warning", "Please select both input and output directories.")
        return
    
    process_directory(input_dir, output_dir)

root = tk.Tk()
root.title("SAXS/WAXS Processing")
root.geometry("500x350")
root.config(bg='light blue')
bg_color = 'light blue'

# Title Label 
tk.Label(root, text="SAXS/WAXS Processing", font=("Arial", 16, "bold"), fg="black", bg=bg_color).pack(pady=10)

# Input Directory Selection
input_dir_var = tk.StringVar()
tk.Label(root, text="Input Directory:", font=("Arial", 10, "bold"),bg=bg_color, fg="black").pack()
tk.Entry(root, textvariable=input_dir_var, width=50).pack()
tk.Button(root, text="Browse", command=select_input_directory, bg="#5381dc").pack(pady=(5, 10), padx=10) 

# Output Directory Selection
output_dir_var = tk.StringVar()
tk.Label(root, text="Output Directory:",font=("Arial", 10, "bold"), bg=bg_color, fg="black").pack()
tk.Entry(root, textvariable=output_dir_var, width=50).pack()
tk.Button(root, text="Browse", command=select_output_directory, bg="#5381dc").pack(pady=(5, 10), padx=10) 

process_type = tk.StringVar(value="temperature")
tk.Label(root, text="Select Data Type:", bg=bg_color, fg="black").pack()


radio_frame = tk.Frame(root, bg=bg_color)
radio_frame.pack()

tk.Radiobutton(radio_frame, text="Temperature", variable=process_type, value="temperature", bg=bg_color).pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="Q (INT)", variable=process_type, value="q_int", bg=bg_color).pack(side=tk.LEFT)

tk.Button(root, text="Start Processing", command=start_processing, bg="green", fg="white", ).pack(pady=20)
root.mainloop()