from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from test import *


def search_file():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
    # Rozbić na funkcje i odpalić w tym miejscu cały algorytm
    run(filename)


class MyWindow:
    def __init__(self, root) -> None:
        self.image = Image.open("img/bg.jpg")
        self.img = self.image.resize((400, 400))
        self.bg = ImageTk.PhotoImage(self.img)
        self.background = Label(root, image=self.bg)
        self.background.place(x=0, y=0)

        self.description = Label(root, text="Description of the algorithm")
        self.description.place(x=0, y=0, width=400, height=50)
        self.description.configure(foreground="white", background="black")
        self.lbl = Label(root, text="Choose file to process, click button below")
        self.lbl.place(x=75, y=75, width=250)
        self.lbl.configure(foreground="white", background="black")

        self.search = Button(root, text='Search', command=search_file, background="black", foreground="white")
        self.search.place(x=150, y=100, w=100, h=50)

