import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import subprocess

class PyGitClient():
    def __init__(self) -> None:
        pass
    def git_init(self):
        pass 

    def git_add(self):
        pass 

    def git_commit(self, message):
        pass 

    def git_push(self):
        pass 

    def git_is_repo(self,path):
       return subprocess.call(['git', '-C', path, 'status'], stderr=subprocess.STDOUT, stdout = open(os.devnull, 'w')) == 0

class PyGitClientGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pygitclient = PyGitClient()
        self.title("py-git")
        self.minsize(width=500, height=750)
        self.gui_create_start_info()
        self.content_frame = None    
      
    def gui_select_dir(self):
        path = StringVar()
        def select_dir():
            dir_path = filedialog.askdirectory()
            if self.pygitclient.git_is_repo(dir_path):
                path.set(dir_path)
            else:
                messagebox.showerror("Error","Directory is not a git repository")
                
        self.gui_clear_frame()
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(padx=5, pady=5, fill="both", expand=True)  

        tk.Button(self.content_frame, text="Select Folder", command=select_dir).pack(padx=10,pady=10)
        tk.Label(self.content_frame,textvariable=path).pack(padx=10,pady=10)
    def gui_make_dir(self):
        self.gui_clear_frame()
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(padx=5, pady=5, fill="both", expand=True)
       
        make = tk.Label(self.content_frame, text="MAKE")
        make.pack(padx=5,pady=5)
    
    def gui_clear_frame(self):
        if self.content_frame:
            self.content_frame.destroy()  
            self.content_frame = None 

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
