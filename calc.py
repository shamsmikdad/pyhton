import tkinter as tk
from tkinter import Entry, ttk


class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("320x200")
        self.title('this is calculater')

        # initialize data
        self.opration = ('+', '-', '*','/')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

        # self.value(self.number1,self.number2)
        

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self,  text='Select your opration:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # option menu
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.opration[0],
            *self.opration,
            # command=self.option_changed
            )

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

       
        # input
        # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        label = ttk.Label(self,  text='first numbe:')
        label.grid(column=0, row=1, sticky=tk.W, **paddings)
        num1= ttk.Entry(self)
        num1.grid(column=1, row=1, sticky=tk.W, **paddings)
        labe2 = ttk.Label(self,  text='secound numbe:')
        labe2.grid(column=0, row=2, sticky=tk.W, **paddings)
        num2 = ttk.Entry(self)
        num2.grid(column=1, row=2, sticky=tk.W, **paddings)
        result=ttk.Button(self,text="result",command=self.option_changed)
        result.grid(column=0, row=3, sticky=tk.W, **paddings)

        num1.pack()
        num2.pack()

        # output label
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=4, sticky=tk.W, **paddings)

    # def value (self,num1,num2):
        
    #     if self.option_var =="+":
    #         res = num1 + num2
    #     elif self.option_var =="-":
    #         res = num1 - num2
    #     elif self.option_var =="*":
    #         res = num1 * num2
    #     elif self.option_var =="/":
    #         res = num1 / num2
    #     return res

    def option_changed(self, *args):
        self.output_label['text'] = f'You result is: {self.number2}'

    

# Self.operation = ('+','-','*','/')
# Self.option_var= stringVar(Self)
# ttk.OptionMenu(Self,operation,).grid(column=0,row=3)
# ttk.Button(frm, text="result",command=_ButtonCommand)


if __name__ == "__main__":
    Calc = Calc()
    Calc.mainloop()
# root = Tk()
# Self= ttk.Frame(Self, padding=10)
# Self.grid()
# ttk.Label(frm, text="this is calc!").grid(column=0, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# ttk.Label(frm, text="first number").grid(column=0,row=1)
# input1 = ttk.Entry(frm).grid(column=1,row=1)
# ttk.Label(frm, text="second").grid(column=0,row=2)
# input2 = ttk.Entry(frm).grid(column=1,row=2)

# frm.operation = ('+','-','*','/')
# frm.option_var= stringVar(frm)
# ttk.OptionMenu(frm,operation,).grid(column=0,row=3)
# # ttk.Button(frm, text="result",command=_ButtonCommand)

# def ButtonCommand (input1,input2):
#     if ()
