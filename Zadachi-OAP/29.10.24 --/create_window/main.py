from tkinter import *

window = Tk()
window.title("Краснодарский Кооперативный Техникум")

window.geometry("640x480")

label = Label(window, text = "Краснодарский Кооперативный Техникум", font = "Arial 16")
label.pack(side="top")

label_1 = Label(window, text = 'Кулешов Олег Сергеевич', font = ("Arial", 24, "bold"))
label_1.pack(padx=150, pady=50)

window.mainloop()
