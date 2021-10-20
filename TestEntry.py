import tkinter as tk

self = tk.Tk()
self.title('this is calculater')
self.geometry("320x200")

self.opration = ('+', '-', '*','/')
self.option_var = tk.StringVar(self)
number1 = int(self.entry1.get())
number2 = int(self.entry2.get())

self.entry1 = tk.Entry(self)
self.entry1.pack()
self.entry2 = tk.Entry(self)
self.entry2.pack()

# option_menu = tk.OptionMenu(
#             self,
#             self.option_var,
#             self.opration[0],
#             *self.opration,
#             # command=self.option_changed
#             )
# option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)
def calcualte (num1,num2):
    res = num1+num2
    return res

def calculator():
    output_label['text'] = f'You result is: {calcualte(number1,number2)}'


button_calc = tk.Button(self,text="calc", command=calculator)
button_calc.pack()

output_label = tk.Label(self,text="labelProSales", foreground='red')
output_label.pack()

self.mainloop()