"""pytext v1.2.0 14:07 07.02.2023 by Youpiter TV"""
from darkdetect import theme as win_theme
from sv_ttk import set_theme
from os.path import exists
from os import system
import tkinter as tk
t = win_theme().lower()
def theme():
    global t
    if t == "dark": t = "light"
    else: t = "dark"
    set_theme(t)
def save():
    try:
        open(file=filename, mode="w").write(inbox.get("0.0", tk.END))
        labtwo["text"] = f"Saved {filename}."
    except:
        labtwo["text"] = f"File {filename} could not be saved."
def read():
        if not exists(filename): labtwo["text"] = f"File {filename} does not exist."; return
        data = open(file=filename, mode="r").read()
        inbox.delete("0.0", tk.END); inbox.insert("0.0", data, tk.END); inbox.update()
        labtwo["text"] = f"Read {filename}."
def openf():
    global filename
    filename = filetext.get()
    if not exists(filename):
        labtwo["text"] = f"File {filename} does not exist."
        return
    labtwo["text"] = f"Opened {filename}."
def run():
    if not exists(filename): labtwo["text"] = f"File {filename} does not exist."; return
    system(f"start {filename}")
filename = "new.txt"
window = tk.Tk()
window.title("pytext v1.2.0")
labone = tk.Label(text="pytext v1.2.0 - made by Youpiter")
labtwo = tk.Label(text=f"Opened {filename}.")
inbox = tk.Text()
filetext = tk.Entry()
readb = tk.Button(text= "Read", command=read); saveb = tk.Button(text="Save", command=save)
openb = tk.Button(text="Open", command=openf); runb = tk.Button(text="Run", command=run)
toggleb = tk.Button(text= "Toggle theme", command=theme)
labone.pack(); inbox.pack()
readb.pack(padx=10, pady=20, side=tk.RIGHT); saveb.pack(padx=10, pady=20, side=tk.LEFT)
labtwo.pack(); filetext.pack(); openb.pack(); runb.pack()
toggleb.pack()
set_theme(t)
window.mainloop()