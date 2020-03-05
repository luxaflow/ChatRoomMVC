from tkinter import *
import threading


class ServerView(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)

        self.__running_label = Label(self, text='Server is running', padx=10)
        self.__running_label.pack()


    def set_labels(self, host, port):

        Label(self, text='On host: {0}'.format(host), padx=10).pack()
        Label(self, text='On port: {0}'.format(port), padx=10).pack()
