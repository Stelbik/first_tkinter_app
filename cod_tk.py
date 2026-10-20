# импортируем модуль tkinter
from curses import window
from tkinter import *
from tkinter import ttk

# создаем главное окно
root = Tk()
root.iconbitmap(default="icon-445309.ico")
# создаем заголовок для окна
root.title("Приложение")
# задаем размеры для окна
root.geometry("600x600")

btn = ttk.Button(text="Нажать")
btn.pack()
# создаем лейбл для вывода текстового сообщения
label = Label(text="Привет")
# размещаем лейбл с помощью метода pack
label.pack()
# вызов главного окна с помощью метода mainloop
root.mainloop()
