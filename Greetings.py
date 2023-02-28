from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.geometry("400x600")

def hello():
    hello_label = Label(root, text="Hello" + my_textbox.get())
    hello_label.pack()

my_label = Label(root, text="Enter your first name:")
my_label.pack()

my_textbox = Entry(root, width=30)
my_textbox.pack()

my_button = Button(root, text="Submit", command=hello)
my_button.pack()

hello_label = Label(root, text="")
hello_label.pack()

root.mainloop()
