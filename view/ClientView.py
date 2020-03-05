from tkinter import *

class ClientView(Frame):
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)

        """
        Controller in the View is only required to bind controller actions
        """
        self.__controller = controller

        self.__message_var = StringVar()
        self.__scrollbar = Scrollbar()

        self.__message_box = Listbox(self, height=15, width=100, yscrollcommand=self.__scrollbar.set)

        self.__scrollbar.pack(side=RIGHT, fill=Y)
        self.__message_box.pack(side=LEFT, fill=BOTH)
        self.__message_box.pack()
        self.__entry_field = Entry(master, width=100, textvariable=self.__message_var)
        self.pack()

        self.__entry_field.pack(side=LEFT)
        self.__entry_field.bind("<Return>", self.__controller.send_message)


    def get_message_var(self):
        msg = self.__message_var.get()
        self.__message_var.set('')
        return msg


    def insert_message_box(self, message):
        self.__message_box.insert(END, message)
