import pytesseract
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pyperclip

window = Tk()

window.title("OCR GUI")

def get_and_open_file():
    global my_image
    window.filename = filedialog.askopenfilename(initialdir="C:/",title="Select A File!",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg"),("all filess","*.*")))
    my_label = Label(window, text=window.filename).pack()

    my_image = ImageTk.PhotoImage(Image.open(window.filename))

    my_image_label = Label(image=my_image).pack()

my_btn = Button(window,text="Open File", command=get_and_open_file).pack()

def get_read_and_write_file():
    window.filename = filedialog.askopenfilename(initialdir="C:/",title="Select A File!",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg"),("all filess","*.*")))
    myconfig = r"--psm 4 --oem 3"

    photo = str(window.filename)
    textt = pytesseract.image_to_string(Image.open(f"{photo}"), lang="tur", config=myconfig)
    pyperclip.copy(textt)
    the_label = Label(window, text=textt).pack()
    

the_btn = Button(window,text="OCR Photo", command=get_read_and_write_file).pack()

window.mainloop()