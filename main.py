from tkinter import *
from gui import MyWindow

if __name__ == '__main__':
    root = Tk()
    mywin = MyWindow(root)
    root.title('Car plate detector')
    root.geometry("400x400")
    root.resizable(False, False)
    root.mainloop()