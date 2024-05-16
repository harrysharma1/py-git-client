import tkinter
from tkinter import Label

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
        self.root = tkinter.Tk()
        self.root.minsize(250,250)

    def setup(self):
        w = Label(self.root, text="Python Git Client")
        w.pack()

    def run(self):
        self.setup()
        self.root.mainloop()



if __name__ == "__main__":
    gui = PyGitClientGUI()
    gui.run()
