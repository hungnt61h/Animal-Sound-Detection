from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Animal Sound Detection")
        self.minsize(600,400)


        self.labelFrame = ttk.LabelFrame(self, text = "Open a file")
        self.labelFrame.grid(column = 0, row = 0, padx = 20, pady =20)
        
        self.button()
    
    def button(self):
        self.labelFrame = ttk.Button(self.labelFrame, text = "Browse a file", command = self.fileDialog)
        self.labelFrame.grid(column = 1, row = 2)

    def fileDialog(self):
        #currdir = os.getcwd()
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetype = (("wav","*.wav"), ("All file","*.*")))
        #folder
        # self.tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        print(" Path: %s" % self.filename)
        return self.filename

if __name__ == "__main__":
    root = Root()
    # root.withdraw()
    root.mainloop()
    # print(" Path: %s" % root.fileDialog())
