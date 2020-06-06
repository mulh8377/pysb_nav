import tkinter as tk
import argparse
import asyncio


import Models.File.v_file as VFile
import Models.Class.v_class as VClass
import Models.Function.v_function as VFunc
#from Models.Build.v_builder import BuilderView
#from Models.Folder.v_folder import FolderView
#from Models.Tester.v_tester import TesterView
#from Models.Refactor.v_refactor import RefactorView
    
def set_root(_geo="600x800"):
    root = tk.Tk()
    root.geometry(_geo)
    return root

def main(choice_type, choice_label):
    view = None
    flag = 1
    if choice_type == "--file":
        view = VFile.FileView(master=set_root())
        view.mainloop()

    elif choice_type == "--class":
        view = VClass.ClassView(master=set_root())
        view.mainloop()

    elif choice_type == "--func":
        view = VFunc.FunctionView(master=set_root(_geo="400x600"))
        view.mainloop()

    elif choice_type == "--build":
        pass
        #view = BuilderView(master=set_root())
        #view.mainloop()

    elif choice_type == "--folder":
        pass
        #view = FolderView(master=set_root(_geo="400x600"))
        #view.mainloop()

    elif choice_type == '--tester':
        pass
        #view = TesterView(master=set_root(_geo="400x600"))

    elif choice_type == "--refactor":
        pass
        #view = RefactorView(master=set_root(_geo="400x600"))
        #view.mainloop()

    elif choice_type == '--config':
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
    parser.add_argument("--new_test", required=False)
    parser.add_argument("--new_refactor", required=False)
    parser.add_argument("--new_folder", required=False)
    parser.add_argument("--new_build", required=False)
    #parser.add_argument("--h", required=False)

    args = parser.parse_args()

    t, l, f = '', '', ''
    if args.new_class:
        t, l, f = main(choice_type="--class", choice_label=args.new_class)
    if args.new_func:
        t, l, f = main(choice_type="--func", choice_label=args.new_func)
    if args.new_file:
        t, l, f = main(choice_type="--file", choice_label=args.new_file)
    if args.new_build:
        t, l, f = main(choice_type="--build", choice_label=args.new_build)
    if args.new_folder:
        t, l, f = main(choice_type="--folder", choice_label=args.new_folder)
    if args.new_test:
        t, l, f = main(choice_type="--test", choice_label=args.new_test)
    if args.new_refactor:
        t, l, f = main(choice_type="--refactor", choice_label=args.new_refactor)
