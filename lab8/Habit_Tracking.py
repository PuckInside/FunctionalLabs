import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, text)

def save_file():
    text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text += "\t" + text_area.get(1.0, tk.END) + "\n"
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

root = tk.Tk()
root.title("Привычкометр")
root.geometry("300x400")

current_datetime = "Привычка, которую хочешь написать:"
date_label = tk.Label(root, text=current_datetime)
date_label.pack()

text_area = tk.Text(root, undo=True)
text_area.pack(fill="both", expand=True)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)

root.mainloop()
