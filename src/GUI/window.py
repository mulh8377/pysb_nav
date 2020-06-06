import tkinter as tk
import subprocess
import asyncio

#from Models.Build.v_builder import BuilderView
#from .Models.Folder.v_folder import FolderView
#from .Models.Tester.v_tester import TesterView
#from .Models.Refactor.v_refactor import RefactorView


class Application(tk.Frame):
    def __init__(self, master=None, menu=None):
        super().__init__(master)
        self.master = master
        self.menu = menu
        self.pack()
        self.init_widgets()
        
    def init_widgets(self):

        self.w_build = self.init_build()
        self.w_config = self.init_config()

        self.w_folder = self.init_folder()
        self.w_file = self.init_file()
        
        self.w_class = self.init_class()
        self.w_function = self.init_function()
        
        self.w_tester = self.init_tester()
        self.w_refactor = self.init_refactor()

        self.w_build.grid(row=0, column=0)
        self.w_config.grid(row=0, column=1)
        
        self.w_folder.grid(row=0, column=2)
        self.w_file.grid(row=1, column=0)
        
        self.w_class.grid(row=1, column=1)
        self.w_function.grid(row=1, column=2)
        
        self.w_tester.grid(row=2, column=0)
        self.w_refactor.grid(row=2, column=2)

    def init_build(self):
        return tk.Button(self, text="BUILD", command=self.event_file)

    def init_config(self):
        return tk.Button(self, text="CONFIG", command=self.event_file)

    def init_folder(self):
        return tk.Button(self, text="FOLDER", command=self.event_file)

    def init_file(self):
        return tk.Button(self, text="FILE", command=self.event_file)

    def init_class(self):
        return tk.Button(self, text="CLASS", command=self.event_class)

    def init_function(self):
        return tk.Button(self, text="FUNCTION", command=self.event_function)

    def init_tester(self):
        return tk.Button(self, text="TEST", command=self.event_function)
    
    def init_refactor(self):
        return tk.Button(self, text="REFACTOR", command=self.event_function)

    def event_file(self, identifier="--new_file", _label="new_file.py"):
        self.sub_window(tag=identifier, label=_label)

    def event_class(self, identifier="--new_class", _label="NewClass"):
        self.sub_window(tag=identifier, label=_label)
        #view = pysb_view.ClassView(master=tk.Tk())
        #return view.mainloop()
    
    def event_function(self, identifier="--new_func", _label="new_function"):
        self.sub_window(tag=identifier, label=_label)
        #view = pysb_view.FileView(master=tk.Tk())
        #return view.mainloop()

    def sub_window(self, tag, label, target="src/views.py", language="python3"):
        subprocess.call([language, target, tag, label])

async def run():
    root=tk.Tk()
    root.geometry("300x100")
    menubar = tk.Menu(master=root)
    root.config(menu=menubar)
    m_project = tk.Menu(menubar)
    menubar.add_cascade(menu=m_project, label="Project")

    app = Application(master=root, menu=menubar)
    app.mainloop()