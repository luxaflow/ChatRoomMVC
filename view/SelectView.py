from tkinter import *


class SelectView(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)

        self.__msg_label = Label(
            self, text='What do you want to start', padx=10)
        self.__msg_label.pack()

        self.__client_button = Button(self, text='Client', width=20, height=3, padx=10)
        self.__client_button.pack()
        self.__client_button.bind('<Button>', controller.start_client)

        self.__server_button = Button(self, text='Server', width=20, height=3, padx=10)
        self.__server_button.pack()
        self.__server_button.bind('<Button>', controller.start_server)
