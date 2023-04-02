"""pytext V1.1.1 14:07 07.02.2023 by Youpiter tv"""
import tkinter as tk
import os
def savefile():
    file = open(filename,"w")
    file.write(inbox.get("0.0",tk.END))
    file.close()
def readfromfile():
    try:
        file = open(filename,"s")
        inbox.delete("0.0",tk.END)
        inbox.insert("0.0",file.read(),tk.END)
        inbox.update()
        file.close()
    except:
        labtwo["text"] = "file not created " + filename
def openfile():
    global filename
    filename = filetext.get()
    labtwo["text"] = "opened "+filename
def runfile():
    os.system("start "+filename)

filename = "new.txt"

window = tk.Tk()
window.title("Pytext 1.1.1")

labone = tk.Label(text="V1.1.1 pytext editor by Youpiter")
labtwo = tk.Label(text="opened "+filename)

inbox = tk.Text()
filetext = tk.Entry()

readb = tk.Button(text= "read",command=readfromfile)
saveb = tk.Button(text="save",command=savefile)
openb = tk.Button(text="open",command=openfile)
runb = tk.Button(text="run", command=runfile)

labone.pack()
inbox.pack()

readb.pack(padx=10, pady=20, side=tk.RIGHT)
saveb.pack(padx=10, pady=20, side=tk.LEFT)

labtwo.pack()
filetext.pack()
openb.pack()

runb.pack()

window.mainloop()