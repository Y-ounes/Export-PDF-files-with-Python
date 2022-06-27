from itertools import tee
from math import ceil
from tkinter import *
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#print('hello world')
root = tk.Tk()
canvas = tk.Canvas(root, width=100, height=200)
canvas.grid(columnspan=3, rowspan=3)
#create logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


##different instruction
instruct = tk.Label(root, text="Select your file", font="Helvetica")
instruct.grid(columnspan=3, column=0, row=1)

##fucntion open
def open_file():
    print("working")
    red_txt.set("Loading")
    file = askopenfile(parent=root, mode='rb', title="Choose your file", filetypes=[("pdf file", "*.pdf")])
    if file:
        red_pdf = PyPDF2.PdfFileReader(file)
        p = red_pdf.getPage(0)
        p_content = p.extractText()
        print(p_content)

## insert text box
        txt_box = tk.Text(root, height=15, width=22, padx=20, pady=33)
        txt_box.insert(1.0, p_content)
        txt_box.grid(column=1, row=3)

## browse test
red_txt = tk.StringVar()
red_btn = tk.Button(root, textvariable= red_txt,command=lambda:open_file(), font="Helvetica",fg="Black", bg="#ff3348",height=2, width=15)
red_txt.set("Read")
red_btn.grid(column=1, row=2)


###
canvas = tk.Canvas(root, width=400, height=250)
canvas.grid(columnspan=3)
root = mainloop()