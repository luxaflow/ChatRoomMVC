from tkinter import *


class ConnectView(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)

        self.__msg_label = Label(self, text='Welcome, press start tot connect to server')
        self.__msg_label.pack()

        Label(self, text='Server').pack()
        self.__host_var = StringVar()
        Entry(self, textvariable=self.__host_var).pack(fill=X)

        Label(self, text='Port').pack()
        self.__port_var = StringVar()
        Entry(self,  textvariable=self.__port_var).pack(fill=X)

        Label(self, text='Username').pack()
        self.__username_var = StringVar()
        Entry(self, textvariable=self.__username_var).pack(fill=X)
        
        self.__button = Button(self, text='Connect')
        self.__button.pack()
        self.__button.bind('<Button>', controller.connect)

        
    def get_port_var(self):
        return int(self.__port_var.get())

    
    def set_port_var(self, value):
        self.__port_var.set(value)


    def get_host_var(self):
        return self.__host_var.get()


    def set_host_var(self, value):
        self.__host_var.set(value)

    
    def get_username_var(self):
        return self.__username_var.get()

