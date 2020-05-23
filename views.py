import tkinter as tk
import argparse
import pyfile as file_ops
import pyclass as class_ops
import pyfunction as function_ops

class FunctionView(tk.Frame):
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
def set_root(_geo="600x800"):
    root = tk.Tk()
    root.geometry(_geo)
    return root

def main(choice_type, choice_label):
    view = None
    flag = 1
    if choice_type == "--file":
        view = FileView(master=set_root())
        view.mainloop()
    elif choice_type == "--class":
        view = ClassView(master=set_root())
        view.mainloop()
    elif choice_type == "--func":
        view = FunctionView(master=set_root(_geo="400x600"))
        view.mainloop()
    elif choice_type == '--help':
        print(choice_label)
        flag = -1
    else:
        flag = 0
    
    return choice_type, choice_label, flag

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--new_class", required=False)
    parser.add_argument("--new_func", required=False)
    parser.add_argument("--new_file", required=False)
    #parser.add_argument("--h", required=False)

    args = parser.parse_args()

    t, l, f = '', '', ''
    if args.new_class:
        t, l, f = main(choice_type="--class", choice_label=args.new_class)
    if args.new_func:
        t, l, f = main(choice_type="--func", choice_label=args.new_func)
    if args.new_file:
        t, l, f = main(choice_type="--file", choice_label=args.new_file)
