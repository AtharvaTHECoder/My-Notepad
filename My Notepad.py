from tkinter import *
from tkinter.filedialog import asksaveasfilename , askopenfilename

filePath = ''

def set_file_path(path):
    global filePath
    filePath = path


def open_file():
    path = askopenfilename(filetypes = [('Text Files', '*.txt')])
    with open(path, 'r' ) as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if filePath == '':
        path = asksaveasfilename(filetypes = [('Text Files', '*.txt')])
    else:
        path = filePath
    with open(path , 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

compiler = Tk()
editor = Text()
editor.pack()
logo = PhotoImage(file = 'notepad.png')
compiler.iconphoto(False,logo)
compiler.title('My Fantastic Notepad')

menuBar = Menu(compiler)

fileBar = Menu(menuBar, tearoff = 0)
fileBar.add_command(label = 'Open', command = open_file)
fileBar.add_command(label = 'Save', command = save_as)
fileBar.add_command(label = 'Save As', command = save_as)
fileBar.add_command(label = 'Exit', command = exit)
menuBar.add_cascade(label = 'File', menu = fileBar)

Bar = Menu(menuBar, tearoff = 0)
compiler.config(menu = menuBar)
compiler.mainloop()