
from tkinter import *
from tkinter import font as tkfont
import Utilities as ut
#import DataScript.DataSp as ds
class TextTickableEditor():
    __canEdit = True

    #get index of row, col
    def get_index(self, key : str) -> int:
        dictIndex = {'col' : self.__lastColIndex, 'row' : self.__lastRowIndex}
        try:
            return dictIndex[key]
        except:
            print("error get key is " + key)
            return dictIndex['col']
    
    #do tick: if tick mean can Edit else can't edit
    def tick_box(self):
        self.__canEdit = not self.__canEdit
        if self.__canEdit:
            self.txt_edit.config(state='normal')
        else:
            self.txt_edit.config(state='disabled')
        pass

    def __init__(self, whatFrame : Frame, iRow : int, iCol : int, idChapter : str, content = ""):
        
        #Save Index
        self.__lastColIndex = iCol
        self.__lastRowIndex = iRow

        #mainFrame
        self.thisFrame = Frame(whatFrame)
        self.thisFrame.grid(row=iRow,column=iCol,sticky="nsew")

        #Text Describe

        self.tk_label = Label(self.thisFrame, text=idChapter)
        self.tk_label.grid(column=0, row=0, stick = "w")

        #text_editor
        self.txt_edit = Text(self.thisFrame, name=idChapter, height=ut.HEIGHT_BOX_TEXT_EDITOR, width = ut.WIDTH_BOX_TEXT_EDITOR)
        self.txt_edit.grid(row=1, column=0, sticky="nsew", **ut.padding) 
        
        self.__canEdit = True
        self.tick_box() 
        #add radio btn
        self.tick_btn = Checkbutton(self.thisFrame, text='edit', variable=self.__canEdit, command=self.tick_box)
        self.tick_btn.grid(row=2, column=0, **ut.padding, sticky='e')

        
class MainFrame(Tk):
    def __init__(self):
        Tk.__init__(self)
        
        #Set font
        self.title_font = tkfont.Font(family='Helvetica', size=13, weight="bold", slant="italic")
        self.title("Project Solution")

        #Design UI Here
        
        #region Main Top Frame
        top_frame = Frame(self, width=100, height=100,bd=1)
        top_frame.grid(row=0,column=1,sticky="nsew")

        #Start from Left Top
        left_top_frame = Frame(top_frame, width=50, height=100, bd=1)
        left_top_frame.grid(row=0,column=0,sticky="nsew")

            #Main Function UI for project work here
        button_left_fnc1 = Button(left_top_frame, width=10, height=5, text="Algorithm 1")
        button_left_fnc2 = Button(left_top_frame, width=10, height=5, text="Algorithm 2")
        button_left_fnc3 = Button(left_top_frame, width=10, height=5, text="Algorithm 3")
        button_left_fnc4 = Button(left_top_frame, width=10, height=5, text="Algorithm 4")
        button_left_fnc5 = Button(left_top_frame, width=10, height=5, text="Algorithm 5")
        
        button_left_fnc1.grid(row=0,column=0,sticky="nsew", **ut.padding)
        button_left_fnc2.grid(row=1,column=0,sticky="nsew", **ut.padding)
        button_left_fnc3.grid(row=2,column=0,sticky="nsew", **ut.padding)
        button_left_fnc4.grid(row=3,column=0,sticky="nsew", **ut.padding)
        button_left_fnc5.grid(row=4,column=0,sticky="nsew", **ut.padding)

        #Start from Middle
        frm_editor = Frame(top_frame, width = 20, height=400,bd=2)
        frm_editor.grid(row = 0, column=1, sticky="nsew")

        #Text Describe
        text_box_1 = TextTickableEditor(frm_editor, 0, 0, "chapter1")
        text_box_2 = TextTickableEditor(frm_editor, 1, 0, "chapter1")
        text_box_3 = TextTickableEditor(frm_editor, 2, 0, "chapter1")
        text_box_4 = TextTickableEditor(frm_editor, 3, 0, "chapter1")
        text_box_5 = TextTickableEditor(frm_editor, 4, 0, "chapter1")


        #Start from Left(Output Alogrithm show here)
        #endregion

if __name__ == "__main__":
    mf = MainFrame()
    mf.mainloop()