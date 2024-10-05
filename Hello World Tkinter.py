from tkinter import * 

windows = Tk()

windows.title("My first program in Tkinter")
windows.geometry("500x500")
windows.resizable(True, True)

label1=Label(windows, text="Hello World Tkinter",
             font=("Comic Sans MS", 25, "bold"),
             bg = "#0488fd",
             fg= "#26fd04",
             bd=5)
label1.pack()
windows.mainloop()