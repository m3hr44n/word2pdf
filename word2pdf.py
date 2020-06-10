#python project
#mehraan kiya
#roshanamooz


import tkinter as tk
from docx2pdf import convert
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
#librarys for needs



win = tk.Tk()

#title for program name or programmer


win.title("word to pdf converter coded by m3hr44n")

def openFile():
    file = askopenfile(filetypes =[('word files', '*.docx')])
    convert(file.name,r'C:\Users\Desktop\converted.pdf')
    showinfo("Done","file successfully converted")

#function for open file 


label = tk.Label(win,text="Choose file => : ")
label.grid(row=1,columns=1,padx=5,pady=5)    

#label grid for size screen program


button = ttk.Button(win,text= "Select",width=30,command=openFile)

button.grid(row=2,column=1,padx=5,pady=5)


win.mainloop()


