from textwrap import fill
import tkinter as tk
import DataScript.DataSp as ds
import UIScript.Utilities as ut


def get_text_from_frame(textFrame : tk.Text) -> str:
    return textFrame.get("1.0", tk.END)


    mainRunner.mainloop()
#def get_changeLayout_2():

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Simple Text Editor")

    window.rowconfigure(0, minsize=200, weight=1)
    window.columnconfigure(1, minsize=400, weight=1)

    
    frm_editor = tk.Frame(window,width = 20, height=400, bd=2)
    txt_edit = tk.Text(frm_editor, height=10, width = 10)

    txt_edit_1 = tk.Text(frm_editor, height=10, width = 10)
    txt_edit_2 = tk.Text(frm_editor, height=10, width = 50)

    frm_editor.grid(row = 0, column=1, sticky="nsew")
    txt_edit.grid(row=0, column=1, sticky="nsew", pady=5,padx=8)
    txt_edit_1.grid(row=1, column=1, sticky="nsew",pady=5,padx=8)
    txt_edit_2.grid(row=2, column=1, sticky="nsew",padx=8,pady=5)

    #window.rowconfigure(2, minsize = 200, weight=1)
    frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    frm_buttons.grid(row=0, column=0, sticky="ns")

    btn_open = tk.Button(frm_buttons, text="Open")
    btn_get1 = tk.Button(frm_buttons, text="Save As 1", command= lambda : print(get_text_from_frame(txt_edit)))
    btn_get2 = tk.Button(frm_buttons, text="Save As 2", command= lambda : print(get_text_from_frame(txt_edit_1)))
    btn_get3 = tk.Button(frm_buttons, text="Save As 3", command= lambda : print(get_text_from_frame(txt_edit_2)))

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_get1.grid(row=1, column=0, sticky="ew", padx=5)
    btn_get2.grid(row=2, column=0, sticky="ew", padx=5)
    btn_get3.grid(row=3, column=0, sticky="ew", padx=5)

    window.mainloop()