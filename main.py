import tkinter as tk
from tkinter import *

class PyGitClient():
    def __init__(self,repo_name) -> None:
        self.repo_name = repo_name

    def git_init(self):
        pass 

    def git_add(self):
        pass 

    def git_commit(self, message):
        pass 

    def git_push(self):
        pass 

class PyGitClientGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("py-git")
        self.minsize(width=500, height=750)
        self.gui_create_start_info()
    
    def gui_select_dir(self):
        select = tk.Label(self)
        select.config(text="SELECT")
    def gui_make_dir(self):
        make = tk.Label(self)
        make.config(text="MAKE")

    def gui_create_start_info(self):
        tk.Label(self,text="Python Git Client").pack(padx=5,pady=5)
        tk.Label(self,text="This is a simple Git client built with Python/Tkinter").pack(padx=5,pady=10)

        def select():
            if choice.get()==1:
                text = "Select the location to create your repository:"
                label.config(text=text)
                self.gui_select_dir()
            else:
                text = "Select a already created git repository:"
                label.config(text=text)
                self.gui_make_dir() 
        choice = IntVar()
        tk.Radiobutton(self, text="Select directory", value=1,  variable=choice, command=select).pack(anchor=W)
        tk.Radiobutton(self, text="Make directory", value=2, variable=choice, command=select).pack(anchor=W)
        label = tk.Label(self)
        label.pack()
if __name__ == "__main__":
    gui = PyGitClientGUI()
    gui.mainloop()
