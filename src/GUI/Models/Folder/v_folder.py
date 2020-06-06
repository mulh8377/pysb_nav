import tkinter as tk

class FolderView(tk.Frame):
    def __init__(self, master=None, h=400, w=600):
        super().__init__(master)
        self.master = master
        self.height, self.width = h, w
        self.pack()
        self.init_widgets()
    def init_widgets(self):
        label_header_column = 0
        basic_row = 0

        self.w_name = tk.Label(self, text="Name:")
        self.w_input = tk.Label(self, text="Input:")
        self.w_output = tk.Label(self, text="Output:")
        self.w_description = tk.Label(self, text="Description:")

        self.w_name.grid(row=basic_row, column=label_header_column, pady=2)
        self.w_input.grid(row=basic_row+1, column=label_header_column, pady=2)
        self.w_output.grid(row=basic_row+2, column=label_header_column, pady=2)
        self.w_description.grid(row=basic_row+3, column=label_header_column, pady=2)

        self.e_name = tk.Entry(self)
        self.e_input = tk.Entry(self)
        self.e_output, self.e_description = tk.Entry(self), tk.Text(self, height=20, width=30)

        self.e_name.grid(row=basic_row, column=label_header_column+1, pady=1)
        self.e_input.grid(row=basic_row+1, column=label_header_column+1, pady=1)
        self.e_output.grid(row=basic_row+2, column=label_header_column+1, pady=1)
        self.e_description.grid(row=basic_row+4, column=label_header_column+1, pady=1)


        self.path_to_file = tk.Entry(master=self, text="Input File Path")
        self.path_to_file.grid(row=basic_row+5, column=label_header_column, pady=2)
        self.function_gen = tk.Button(self, text="Generate Function", command=self.event_prepare)
        self.function_gen.grid(row=basic_row+5, column=label_header_column+1,pady=1)
    
    def event_prepare(self):
        print(self.e_name, self.e_input, self.e_output, self.e_description)
