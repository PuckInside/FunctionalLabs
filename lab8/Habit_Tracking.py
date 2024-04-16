import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def open_file():
    file_path = "OneDrive\Рабочий стол\Study\Functional\lab8\Habits.txt"
    if file_path:
        with open(file_path, "r") as file:      
            text = file.read()

        view_file_window = tk.Toplevel(root)
        view_file_window.title("Просмотр привычек")
        text_area_view = tk.Text(view_file_window, undo=False)
        text_area_view.pack(fill="both", expand=True)
        text_area_view.insert(tk.END, text)
        text_area_view.config(state="disabled")


def save_file():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"[ {time} ]"
    text += "\t" + text_area.get(1.0, tk.END) + "\n"

    file_path = "OneDrive\Рабочий стол\Study\Functional\lab8\Habits.txt"
    with open(file_path, "a") as file:
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
file_menu.add_command(label="Просмотр", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)

root.mainloop()
