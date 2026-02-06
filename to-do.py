import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x450")
root.resizable(False, False)

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, task + " ✔")
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# UI Components
label = tk.Label(root, text="My To-Do List", font=("Arial", 18))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

listbox = tk.Listbox(root, width=35, height=10, font=("Arial", 12))
listbox.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=1, column=1, padx=5, pady=5)

# Run application
root.mainloop()
