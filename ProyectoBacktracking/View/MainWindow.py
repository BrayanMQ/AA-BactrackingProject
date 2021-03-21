# IMPORTS
import tkinter as tk


# CLASSES
class Window:

    PAD = 50

    def __init__(self, controller):
        '''
            Constructor
        '''

        self.controller = controller
        self.window = self.createMainWindow()
        self.createButtons("hola", self.controller.hola, 2, 1)

    def createMainWindow(self):
        '''
        '''

        #Window
        window = tk.Tk()
        window.title('BackTracking Proyect')
        window.geometry('500x500')
        window.configure(background='red')

        #Frame

        #Buttons

        return window

    def createButtons(self, text, function, row, column):
        button = tk.Button(self.window, text=text, width="10", command=function).grid(row=row, column=column, padx=self.PAD)
        return button

    def main(self):
        self.window.mainloop()

