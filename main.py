# Alt+3 Studio
# Ilya Katkov
# Я ДОЛЖЕН

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog
from functions import db

# показываем окно
def show_window():

    # вставка результата запроса в таблицу
    def show_in_table(query_func):
        global table_rows
        table_rows = []
        for i in table.get_children():
            table.delete(i)
        for row in query_func:
            if row[3] == "+":
                table.insert('', 'end', values = [query_func.index(row)+1, row[1]], tags = ("done",))
            else:
                table.insert('', 'end', values = [query_func.index(row)+1, row[1]], tags = ("not_done",))
            table_rows.append(row)


    # удаление задач
    def delete_row():
        global table_rows
        rows = [table.item(x)['values'] for x in table.selection()]
        if len(rows) > 1:
            result = mb.askokcancel("Удалить задачи?", "Вы действительно хотите удалить выделенные задачи?")
        else:
            result = mb.askokcancel("Удалить задачу?", "Вы действительно хотите удалить задачу?")
        if result == True:
            for row in rows:
                db.delete_from_table(table_rows[int(row[0])-1][2])
            show_in_table(db.select_in_table())
            root.focus_set()
            btn_del['state'] = 'disabled'

    class custom_ask(simpledialog.Dialog):
        def buttonbox(self):
            '''add standard button box.
            override if you do not want the standard buttons
            '''

            box = Frame(self)
            self.lbl = Label(box, text = "Введите новую задачу:")
            self.lbl.pack(side=TOP, padx=5)
            self.ent = Entry(box)
            self.ent.pack(side=TOP, padx=5, pady=5)
            self.ent.focus_set()
            w = Button(box, text="Добавить", width=10, command=self.ok, default=ACTIVE)
            w.pack(side=LEFT, padx=5, pady=5)
            w = Button(box, text="Отмена", width=10, command=self.cancel)
            w.pack(side=LEFT, padx=5, pady=5)

            self.bind("<Return>", self.ok)
            self.bind("<Escape>", self.cancel)
            box.pack()

        def ok(self, event=None):
            print(self.ent.get())
            db.insert_in_table(self.ent.get())
            show_in_table(db.select_in_table())
            try:
                self.apply()
            finally:
                self.cancel()  

        def cancel(self, event=None):
            # put focus back to the parent window
            if self.parent is not None:
                self.parent.focus_set()
            self.destroy()

    # добавление строки
    def add_window():
        s = custom_ask(root)
        print(s)

    # активация кнопки удаления на кнопку
    def on_select(event):
        btn_del['state'] = 'normal'

    root.geometry("250x450+" + str(x-250) + "+0")
    root.attributes("-alpha", 1)
    lbl_logo = Label(root, text = "Я ДОЛЖЕН", font = "Calibri 20", bg = "white", width = 18)
    lbl_logo.place(x = 0, y = 0)

    btn_sh = Button(root, text = "|", height = 30, command = hide_window, bg = "SteelBlue1", fg = "white")
    btn_sh.place(x = 0, y = 0)

    table = ttk.Treeview(root, columns = ("empty"), show='headings', height = 15)
    table['columns'] = ("id", "task")
    table.column("id", width = 25, anchor = CENTER)
    table.column("task", width = 170, anchor = CENTER)
    table.heading("id", text = "№")
    table.heading("task", text = "Задача")
    table.place(x = 32, y = 48)
    table.bind('<<TreeviewSelect>>', on_select)

    style = ttk.Style()
    table.tag_configure('done', font=('Calibri', 11, "overstrike")) # зачеркиваем текст
    table.tag_configure('not_done', font=('Calibri', 11, "normal"))
    style.configure("Treeview.Heading", font=('Calibri', 13))

    show_in_table(db.select_in_table())

    # table.insert('', 'end', values = [1, "Доделать \"Я должен\""])
    # table.insert('', 'end', values = [2, "Приготовить покушОть"])
    # table.insert('', 'end', values = [3, "Выступить на 2-ом питче"])
    # table.insert('', 'end', values = [4, "Выполнить дз по ИСИС"])

    # ставим задачу выполненной
    def done():
        global table_rows
        rows = [table.item(x)['values'] for x in table.selection()]
        for row in rows:
            db.set_done(table_rows[int(row[0])-1][2])
        show_in_table(db.select_in_table())
        root.focus_set()
        btn_del['state'] = 'disabled'

    add_image = PhotoImage(file = "buttons/add.png")
    done_image = PhotoImage(file = "buttons/done.png")
    remove_image = PhotoImage(file = "buttons/remove.png")

    btn_check = Button(root, command = done, bg='white', bd=0, image=done_image, compound=TOP)
    btn_check.image = done_image
    btn_check.place(x = 57, y = 380)

    btn_add = Button(root, bg='white', bd=0, image=add_image, compound=TOP, command = add_window)
    btn_add.image = add_image
    btn_add.place(x = 109, y = 380)

    btn_del = Button(root, command = delete_row, state = 'disabled', bg='white', bd=0, image=remove_image, compound=TOP)
    btn_del.image = remove_image
    btn_del.place(x = 163, y = 380)

# скрываем окно
def hide_window():
    root.geometry("15x450+" + str(x-15) + "+0")
    root.attributes("-alpha", 0.6)
    btn_sh = Button(root, text = "|", height = 30, command = show_window, bg = "SteelBlue1", fg = "white")
    btn_sh.place(x = 0, y = 0)

root = Tk()
root.title("Я должен")
x = root.winfo_screenwidth()
root.geometry("250x450+" + str(x-250) + "+0")
root.resizable(False, False)
root.lift()
root.attributes("-topmost", True)
root.overrideredirect(1)
root['bg'] = "white"



table_rows = [] # массив всех задач

show_window() # показать окно

root.mainloop()