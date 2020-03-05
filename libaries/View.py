import tkinter as tk

class View(tk.Tk):

    """
    Betreft het Window waarin alle Views geladen kunnen worden
    Deze klasse kan niet overerft worden omdat hiermee het Window meerderee instanties gaat maken.
    Daarna is het niet meer mogelijk te weten in welk window de applicatie draait
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('ChatRoom')
        self.resizable(False, False)
        self.geometry('500x300')

        self.__frame = None 

    """
    Hiermee worden nieuwe view in het window geladen
    Tevens worden oude Views gestopt
    """
    def load_frame(self, frame, controller):
        new_frame = frame(self, controller)
        if self.__frame is not None:
            self.__frame.pack_forget()
            self.__frame.destroy()
        self.__frame = new_frame
        self.__frame.pack()
        controller.set_current_view(self.__frame)
