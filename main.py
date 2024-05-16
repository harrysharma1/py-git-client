import os
import tkinter
from tkinter import Label
from tkinter import filedialog
import tkinter.messagebox

class PyGitClient:
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

class PyGitClientGUI:
    def __init__(self) -> None:
        self.path = ""
        self.dir = ""
        self.root = tkinter.Tk()
        self.root.minsize(width=450,height=600)

    def select_path(self):
        p = filedialog.askdirectory()
        self.path = p
    
    def make_dir(self):
        dirs = os.path.join(self.path,self.dir)
        if not os.path.exists(dirs):
            os.mkdir(dirs)
            tkinter.messagebox.showinfo('Tips:','Folder name created successfully!')
        else:
            tkinter.messagebox.showerror('Tips','The folder name exists, please change it')
 
    def setup(self):
        title = tkinter.Label(self.root, text="Python Git Client")
        title.pack(padx=5,pady=5)
        information = tkinter.Label(self.root, text="This is a simple Git client made with tkinter")
        information.pack(padx=5,pady=10)


    def run(self):
        self.setup()
        self.root.mainloop()



if __name__ == "__main__":
    gui = PyGitClientGUI()
    gui.run()
