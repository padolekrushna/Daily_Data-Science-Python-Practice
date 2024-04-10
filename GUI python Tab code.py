Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> r = tk.Tk()  #instance of class
>>> # type of Widgets
>>> # 1)create label txt
>>> greeting = tk.Label(text="Hello, I am Krushna Pdole")
>>> greeting.pack()    #display the txt
>>> r.geometry('500x500')   #size of tab created
''
>>> # 2)create button
>>> button=tk.Button(text="Click me To view my profile",width=25,height=5,bg="red",fg="blue")
>>> button.pack()
>>> KeyboardInterrupt
>>> #3) Entry
>>> greeting = tk.Label(text="Ask me Quations :")
>>> entry = tk.Entry()
>>> greeting.pack()
>>> entry.pack()
>>> name = entry.get()
>>> name
'how are you'
>>> #method secound to instert input are :
>>> greeting = tk.Label(text="Name of student :")
>>> greeting.pack()
>>> entry = tk.Entry()
>>> entry.pack()
>>> entry.insert(0, "Krushna Padole ")
>>> entry.delete(0)
>>> #4)Getting Multiline User Input With Text Widgets
>>> r = tk.Tk()
>>> text_box = tk.Text()
>>> text_box.pack()
>>> text_box.insert(tk.END, "Put me at the end!")
>>> #5) Frame widgets
>>> frame = tk.Frame()
>>> label = tk.Label(master=frame)
>>> frame.pack()
>>> # we have creates a blank Frame widget and assigns it to the main application window.
>>> #An empty Frame widget is practically invisible
>>> label = tk.Label(master=frame, text="I'm in Frame of profile" width=25,height=5)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> label = tk.Label(master=frame, text="I'm in Frame of profile",width=25,height=5)
>>> label.pack()
