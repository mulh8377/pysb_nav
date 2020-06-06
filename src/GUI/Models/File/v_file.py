import tkinter as tk

class FileView(tk.Frame):

    def __init__(self, master=None, h=600, w=800):

        super().__init__(master)
        self.master = master
        self.height, self.width = h, w
        self.pack()
        self.init_widgets()
        

    def init_widgets(self):
        label_header_column = 0
        basic_row = 0

        self.w_name = tk.Label(self, text="Name:")
        self.w_author = tk.Label(self, text="Author:")
        self.w_date = tk.Label(self, text="Date:")
        self.w_description = tk.Label(self, text="Description:")
        
        self.w_name.grid(row=basic_row, column=label_header_column, pady=2)
        self.w_author.grid(row=basic_row+1, column=label_header_column, pady=2)
        self.w_date.grid(row=basic_row+2, column=label_header_column, pady=2)
        self.w_description.grid(row=basic_row+8, column=label_header_column, pady=2)


        self.w_args = tk.Label(self, text="Arguments:")
        self.w_imports = tk.Label(self, text="Imports:")
        self.w_objects = tk.Label(self, text="Objects:")

        self.w_args.grid(row=basic_row+3, column=label_header_column, pady=2)
        self.w_imports.grid(row=basic_row+4, column=label_header_column, pady=2)
        self.w_objects.grid(row=basic_row+5, column=label_header_column, pady=2)

        

        self.e_name = tk.Entry(master=self)
        self.e_author = tk.Entry(master=self)
        self.e_date = tk.Entry(master=self)
        self.e_description = tk.Text(master=self, height=30, width=30)

        self.e_name.grid(row=basic_row, column=label_header_column+1, pady=2)
        self.e_author.grid(row=basic_row+1, column=label_header_column+1, pady=2)
        self.e_date.grid(row=basic_row+2, column=label_header_column+1, pady=2)
        self.e_description.grid(row=basic_row+9, column=label_header_column+1,pady=2)


        self.e_args = tk.Entry(master=self)
        self.e_imports = tk.Entry(master=self)
        self.e_objects = tk.Entry(master=self)

        self.e_args.grid(row=basic_row+3, column=label_header_column+1, pady=2)
        self.e_imports.grid(row=basic_row+4, column=label_header_column+1, pady=2)
        self.e_objects.grid(row=basic_row+5, column=label_header_column+1, pady=2)


        self.path_to_file = tk.Entry(master=self, text="Input File Path")
        self.path_to_file.grid(row=10, column=label_header_column, pady=2)
        self.file_generator = tk.Button(master=self, text="Generate File", command=self.event_prepare)
        self.file_generator.grid(row=10, column=label_header_column+1, pady=2)
        #self.w_name.pack(side="top")
    
    def event_prepare(self):
        header_fields = [self.e_name, self.e_author, self.e_date, self.e_description]
        footer_fields = [self.e_args, self.e_imports, self.e_objects]
        print(header_fields, footer_fields)
