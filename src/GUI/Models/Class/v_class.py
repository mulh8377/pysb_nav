import tkinter as tk

class ClassView(tk.Frame):
    def __init__(self, master=None, h=600, w=800):
        super().__init__(master)
        self.master = master
        self.height, self.width = h, w
        self.pack()
        self.init_widgets()
        label_header_column = 0
        basic_row = 0
    def init_widgets(self):
        basic_row = 0
        label_header_column = 0
        self.w_name = tk.Label(self, text="Object Name:")
        self.w_public_f = tk.Label(self, text="Object Inherits:")
        self.w_private_f = tk.Label(self, text="Object Fields:")
        self.w_description = tk.Label(self, text="Object Description:")
        
        self.w_name.grid(row=basic_row, column=label_header_column)
        self.w_public_f.grid(row=basic_row+1, column=label_header_column)
        self.w_private_f.grid(row=basic_row+2, column=label_header_column)
        self.w_description.grid(row=basic_row+6, column=label_header_column)

        self.w_setters = tk.Label(self, text="Mutator Methods:")
        self.w_accessors = tk.Label(self, text="Accessor Methods:")

        #self.w_constructor.grid(row=basic_row+3, column=label_header_column)
        self.w_setters.grid(row=basic_row+3, column=label_header_column)
        self.w_accessors.grid(row=basic_row+4, column=label_header_column)

        

        self.e_name = tk.Entry(master=self)
        self.e_public_f = tk.Entry(master=self)
        self.e_private_f = tk.Entry(master=self)
        self.e_description = tk.Text(master=self, height=30, width=25)

        self.e_name.grid(row=basic_row, column=label_header_column+1, pady=1)
        self.e_public_f.grid(row=basic_row+1, column=label_header_column+1, pady=1)
        self.e_private_f.grid(row=basic_row+2, column=label_header_column+1, pady=1)
        self.e_description.grid(row=basic_row+7, column=label_header_column)


        self.e_setters = tk.Entry(master=self)
        self.e_accessors = tk.Entry(master=self)

        #self.e_constructor.grid(row=basic_row+3, column=label_header_column+1, pady=1)
        self.e_setters.grid(row=basic_row+3, column=label_header_column+1, pady=1)
        self.e_accessors.grid(row=basic_row+4, column=label_header_column+1, pady=1)

        self.e_over_str = tk.Radiobutton(master=self, text="__str__")
        self.e_over_hash = tk.Radiobutton(master=self, text="__hash__")
        self.e_over_copy, self.e_over_deepcopy = tk.Radiobutton(master=self,text="__copy__"), tk.Radiobutton(master=self, text="__deepcopy__")

        self.e_over_bool = tk.Radiobutton(master=self, text="__bool__")
        self.e_over_call = tk.Radiobutton(master=self, text="__call__")
        self.e_over_del, self.e_over_new = tk.Radiobutton(master=self,text="__del__"), tk.Radiobutton(master=self, text="__new__")


        self.e_over_str.grid(row=basic_row, column=label_header_column+2)
        self.e_over_hash.grid(row=basic_row+1, column=label_header_column+2)
        self.e_over_copy.grid(row=basic_row+2, column=label_header_column+2)
        self.e_over_deepcopy.grid(row=basic_row+3, column=label_header_column+2)


        self.e_over_bool.grid(row=basic_row+4, column=label_header_column+2)
        self.e_over_call.grid(row=basic_row+5, column=label_header_column+2)
        self.e_over_del.grid(row=basic_row+6, column=label_header_column+2)
        self.e_over_new.grid(row=basic_row+6, column=label_header_column+1)

        self.path_to_file = tk.Entry(master=self, text="Input File Path")
        self.path_to_file.grid(row=10, column=label_header_column+1, pady=2)
        self.class_generator = tk.Button(master=self, text="Generate Class", command=self.event_prepare)
        self.class_generator.grid(row=10, column=label_header_column+2, pady=2)
        #self.w_name.pack(side="top")
    
    def event_prepare(self):
        print("None")
        #header_fields = [self.e_name, self.e_author, self.e_date, self.e_description]
        #footer_fields = [self.e_args, self.e_imports, self.e_objects]
        #print(header_fields, footer_fields)