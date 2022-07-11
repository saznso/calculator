import tkinter as tk

calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
        
    except:
        clear_field()
        text_result.insert(1.0, 'error')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

root = tk.Tk()

frame = tk.Frame(root, bg = 'lavender')
frame.grid(column = 0, row = 0, padx = 5, pady = 5)

text_result = tk.Text(frame, bg = 'white', fg = 'black', height = 2, width = 20, font = ('calibri bold', 24))
text_result.grid(columnspan = 5, pady = 5, padx = 5, sticky = 'ew')

btn_1 = tk.Button(frame, text = '1', highlightbackground = 'lavender', command = lambda:add_to_calculation(1), width = 5,height = 2, font = ('calibri bold', 14))
btn_1.grid(row = 2, column = 1, pady = 5, padx = 5 )

btn_2 = tk.Button(frame, text = '2', highlightbackground = 'lavender', command = lambda:add_to_calculation(2), width = 5,height = 2, font = ('calibri bold', 14))
btn_2.grid(row = 2, column = 2, pady = 5, padx = 5)

btn_3 = tk.Button(frame, text = '3', highlightbackground = 'lavender', command = lambda:add_to_calculation(3), width = 5,height = 2, font = ('calibri bold', 14))
btn_3.grid(row = 2, column = 3, pady = 5, padx = 5)

btn_4 = tk.Button(frame, text = '4', highlightbackground = 'lavender', command = lambda:add_to_calculation(4), width = 5,height = 2, font = ('calibri bold', 14))
btn_4.grid(row = 3, column = 1, pady = 5, padx = 5)

btn_5 = tk.Button(frame, text = '5', highlightbackground = 'lavender', command = lambda:add_to_calculation(5), width = 5,height = 2, font = ('calibri bold', 14))
btn_5.grid(row = 3, column = 2, pady = 5, padx = 5)

btn_6 = tk.Button(frame, text = '6', highlightbackground = 'lavender', command = lambda:add_to_calculation(6), width = 5,height = 2, font = ('calibri bold', 14))
btn_6.grid(row = 3, column = 3, pady = 5, padx = 5)

btn_7 = tk.Button(frame, text = '7', highlightbackground = 'lavender', command = lambda:add_to_calculation(7), width = 5,height = 2, font = ('calibri bold', 14))
btn_7.grid(row = 4, column = 1, pady = 5, padx = 5)

btn_8 = tk.Button(frame, text = '8', highlightbackground = 'lavender', command = lambda:add_to_calculation(8), width = 5,height = 2, font = ('calibri bold', 14))
btn_8.grid(row = 4, column = 2, pady = 5, padx = 5)

btn_9 = tk.Button(frame, text = '9', highlightbackground = 'lavender', command = lambda:add_to_calculation(9), width = 5,height = 2, font = ('calibri bold', 14))
btn_9.grid(row = 4, column = 3, pady = 5, padx = 5)

btn_0 = tk.Button(frame, text = '0', highlightbackground = 'lavender', command = lambda:add_to_calculation(0), width = 5,height = 2, font = ('calibri bold', 14))
btn_0.grid(row = 5, column = 2, pady = 5, padx = 5)

btn_open_parenthesis = tk.Button(frame, text = '(', highlightbackground = 'lavender', command = lambda:add_to_calculation('('), width = 5,height = 2, font = ('calibri bold', 14))
btn_open_parenthesis.grid(row = 5, column = 1, pady = 5, padx = 5)

btn_close_parenthesis = tk.Button(frame, text = ')', highlightbackground = 'lavender', command = lambda:add_to_calculation(')'), width = 5,height = 2, font = ('calibri bold', 14))
btn_close_parenthesis.grid(row = 5, column = 3, pady = 5, padx = 5)

btn_plus = tk.Button(frame, text = '+', highlightbackground = 'lavender', command = lambda:add_to_calculation('+'), width = 5,height = 2, font = ('calibri bold', 14))
btn_plus.grid(row = 2, column = 4, pady = 5, padx = 5)

btn_minus = tk.Button(frame, text = '-', highlightbackground = 'lavender', command = lambda:add_to_calculation('-'), width = 5,height = 2, font = ('calibri bold', 14))
btn_minus.grid(row = 3, column = 4, pady = 5, padx = 5)

btn_multiplication = tk.Button(frame, text = '*', highlightbackground = 'lavender', command = lambda:add_to_calculation('*'), width = 5,height = 2, font = ('calibri bold', 14))
btn_multiplication.grid(row = 4, column = 4, pady = 5, padx = 5)

btn_division = tk.Button(frame, text = '/', highlightbackground = 'lavender', command = lambda:add_to_calculation('/'), width = 5,height = 2, font = ('calibri bold', 14))
btn_division.grid(row = 5, column = 4, pady = 5, padx = 5)

btn_clear = tk.Button(frame, text = 'C', highlightbackground = 'lavender', command = clear_field, width = 15,height = 2, font = ('calibri bold', 14))
btn_clear.grid(row = 6, column = 1, columnspan = 2, pady = 5, padx = 5)

btn_equals = tk.Button(frame, text = '=', highlightbackground = 'lavender', command = evaluate_calculation, width = 15,height = 2, font = ('calibri bold', 14))
btn_equals.grid(row = 6, column = 3, columnspan = 2, pady = 5, padx = 5)


root.mainloop()
