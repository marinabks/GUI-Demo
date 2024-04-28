from tkinter import *
from tkinter import messagebox
import tkinter as tk

# App
class App(tk.Tk):
    def hello_callback(self):
        messagebox.showinfo("Button Demo", "ok")
    
    def exit_app(self):
        self.destroy()
    
    def __init__(self):
        super().__init__()

        self.title("GUI demo")
        self.geometry("1500x300")

        # Frame
        frame1 = tk.Frame(self, borderwidth=2, relief="ridge")
        frame1.pack(side="left")

        frame2 = tk.Frame(self, borderwidth=2, relief="ridge")
        frame2.pack(side="left")

        frame3 = tk.Frame(self, borderwidth=2, relief="ridge")
        frame3.pack(side="left")

        frame4 = tk.Frame(self, borderwidth=2, relief="ridge")
        frame4.pack(side="left")

        frame5 = tk.Frame(self, borderwidth=2, relief="raised")
        frame5.pack(side="left")

        frame6 = tk.Frame(self, borderwidth=2, relief="raised")
        frame6.pack(side="left")

        frame7 = tk.Frame(self, borderwidth=2, relief="raised")
        frame7.pack(side="left")

        # Canvas
        canvas = Canvas(frame1, bg="blue", height=250, width=300)
        coord = 10, 50, 240, 210
        arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
        line = canvas.create_line(10, 10, 200, 200, fill="white")
        canvas.pack(side="left")

        # Button
        button = Button(frame2, text="Hello", command=self.hello_callback)
        button.pack(side="left")

        # Checkbox
        CheckVar1 = IntVar()
        C1 = Checkbutton(frame2, text = "Check Button", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
        C1.pack(side="left")

        # Entry & Label
        L1 = Label(frame4, text="User Name")
        L1.pack(side=LEFT)
        E1 = Entry(frame4, bd=5)
        E1.pack(side=RIGHT)

        # Listbox
        Lb1 = Listbox(frame3)
        Lb1.insert(1, "Python")
        Lb1.insert(2, "Perl")
        Lb1.insert(3, "C")
        Lb1.insert(4, "PHP")
        Lb1.pack(side = "left")

        # Menu
        menu_bar = tk.Menu(self)

        # Create a File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Create an Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")

        # Add the File and Edit menus to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.config(menu=menu_bar)

        # Create a Menubutton widget
        menu_button = tk.Menubutton(frame2, text="Options", relief="raised")
        menu_button.pack(side="left")

        # Create a menu for the Menubutton
        menu = tk.Menu(menu_button, tearoff=0)
        menu.add_command(label="Do nothing", command=self.hello_callback)
        menu.add_command(label="Exit", command=self.exit_app)

        # Attach the menu to the Menubutton
        menu_button.config(menu=menu)

        # Message
        message = tk.Message(frame5, text="This is a message.")
        message.pack(side="left")

        # Radiobutton
        radio = tk.Radiobutton(frame6, activebackground="blue", text="Radio button")
        radio.pack(side="left")

        # Scale
        scale = tk.Scale(frame7, from_=0, sliderlength=20)
        scale.pack(side="left")

if __name__ == "__main__":
    app = App()
    app.mainloop()