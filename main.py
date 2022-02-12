import tkinter as tk
import sqlite3
import easygui
root = tk.Tk()
file = sqlite3.connect("database.db")
cur = file.cursor()
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
def execute():
    try:
        result = codebar.get(1.0, tk.END + "-1c")
        cur.execute(result)
    except sqlite3.Error as er:
        terminal['text'] = er
        codebar.configure(foreground="red")
def open_fileexplorer():
    easygui.fileopenbox()
terminal = tk.Label(bg="black",fg="white", width=root.winfo_screenwidth(), height="32", anchor='nw', border="0")
codebar = tk.Text(root, width=root.winfo_screenwidth(), height="30", border="0")
codebar.pack()
terminal.pack()
button = tk.Button(root, height=1, width=root.winfo_screenwidth(), text="Execute", command=execute)
file_button = tk.Button(root, height=1, width=root.winfo_screenwidth(), text="Select database", command=open_fileexplorer, border=0)
file_button.pack()
button.pack()
root.mainloop()
