# IMPORTS
#import tkinter as tk
from tkinter import *

# CLASSES
from tkinter.ttk import Combobox


class Window:
    PAD = 20
    WIDHTWINDOW = 850
    HEIGHTWINDOW = 650

    # Componentes de la ventana
    window = None
    frame = None
    entryRES = None
    comboboxALGOR = None
    lblSolution = lblRestriction = None
    buttonSolution = buttonRestriction = buttonExecute = buttonRestore = None
    textSolution = textRestriction = textProcedure = None

    def __init__(self, controller):
        '''
            Constructor
        '''

        self.controller = controller
        self.createMainWindow()
        self.disabledButtons()

    def createMainWindow(self):
        '''
        Function: This function is responsible for creating the main window
        Inputs:
        Outputs:
        '''

        # Window
        self.window = self.createWindow('BackTracking Proyect', 'white')

        #Frame
        self.frame = self.createFrame(self.window, 0, 0, self.WIDHTWINDOW-80, self.HEIGHTWINDOW-80)

        # Labels
        self.lblSolution = self.createLabel(self.frame, "Solution: ", 20, 20, 120, 70)
        self.lblRestriction = self.createLabel(self.frame, "Restriction: ", 20, 110, 120, 70)

        #Entry
        self.entryRES = self.createEntry(self.frame, 660, 110, 130, 35)

        #TextArea
        self.textSolution = self.createText(self.frame, 165, 20, 470, 70)
        self.textRestriction = self.createText(self.frame, 165, 110, 470, 70)
        self.textProcedure = self.createText(self.frame, 20, 200, 400, 300)

        #ComboBox
        self.comboboxALGOR = self.createComboBox(self.frame, 180, 520, 130, 35)
        self.comboboxALGOR["values"] = ["Backtraking", "Brute Force"]

        # Buttons
        self.buttonSolution = self.createButtons(self.frame,"Generate Solution", self.controller.solutionFunction,
        660, 40, 130, 35)
        self.buttonRestriction = self.createButtons(self.frame, "Generate Restrictions", self.controller.restrictionFunction,
        660, 145, 130, 35)
        self.buttonExecute = self.createButtons(self.frame,"Execute Algorithm", self.controller.procedureFunction,
        20, 520, 130, 35)
        self.buttonRestore = self.createButtons(self.frame, "Restore", self.controller.restoreFunction,
        650, 520, 130, 35)

    def createWindow(self, pTitle, pBackground):
        '''
        Function: This function is responsible for creating a window with a title and the background color
        Inputs: Title, Background color
        Outputs: Window
        '''

        window = Tk()
        window.resizable(width=False, height=False)
        window.title(pTitle)

        # Window location = center of screen
        x_window = window.winfo_screenwidth() // 2 - self.WIDHTWINDOW // 2
        y_window = window.winfo_screenheight() // 2 - self.HEIGHTWINDOW // 2
        position = str(self.WIDHTWINDOW) + "x" + str(self.HEIGHTWINDOW) + "+" + str(x_window) + "+" + str(y_window)

        window.geometry(position)
        window.configure(background=pBackground)
        return window

    def createFrame(self, pComponent, pRow, pColumn, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a frame
        Inputs: Frame Place, Row, Column, Width, Height
        Outputs: Frame
        '''
        frame = Frame(pComponent, width=pWidth, height=pHeight, highlightbackground='red', highlightthicknes=3)
        frame.grid(row=pRow, column=pColumn, padx=self.PAD, pady=self.PAD, ipadx=self.PAD, ipady=self.PAD)
        frame.grid_propagate(False)
        return frame

    def createLabel(self, pComponent, pText, pX, pY, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a Label
        Inputs: Label Place, Label Text, X, Y, Width, Height
        Outputs: Label
        '''
        label = Label(pComponent, text=pText)
        label.configure(font=("Tahoma", 12, "italic"), relief='sunken', bd=5)
        label.place(x=pX, y=pY, width=pWidth, height=pHeight)
        return label

    def createEntry(self, pComponent, pX, pY, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a Entry
        Inputs: Entry Place, X, Y, Width, Height
        Outputs: Entry
        '''
        entry = Entry(pComponent)
        entry.configure(font=("Tahoma", 10, "italic"), bd=5)
        entry.place(x=pX, y=pY, width=pWidth, height=pHeight)
        return entry

    def createText(self, pComponent, pX, pY, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a TextArea
        Inputs: TextArea Place, X, Y, Width, Height
        Outputs: TextArea
        '''
        text = Text(pComponent)
        text.config(font=("Consolas", 12), bd=5)
        text.place(x=pX, y=pY, width=pWidth, height=pHeight)
        return text

    def createComboBox(self, pComponent, pX, pY, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a ComboBox
        Inputs: ComboBox Place, X, Y, Width, Height
        Outputs: ComboBox
        '''
        combobox = Combobox(pComponent)
        combobox.place(x=pX, y=pY, width=pWidth, height=pHeight)
        return combobox

    def createButtons(self, pComponent, pText, pCommand, pX, pY, pWidth, pHeight):
        '''
        Function: This function is responsible for creating a Button
        Inputs: Button Place, Button Text, Function, X, Y, Width, Height
        Outputs: Button
        '''
        button = Button(pComponent, text=pText, command=pCommand)
        button.configure(font=("Tahoma", 10, "italic"), bd=5)
        button.place(x=pX, y=pY, width=pWidth, height=pHeight)
        return button

    def disabledButtons(self):
        '''
        Function: This function is responsible for disabled all the frame components
        Inputs:
        Outputs:
        '''
        #Solution
        self.buttonSolution.configure(state="normal")

        #Restriction
        self.lblRestriction.configure(state="disabled")
        self.textRestriction.configure(state="disabled")
        self.buttonRestriction.configure(state="disabled")
        self.entryRES.configure(state="disabled")

        #Procedure
        self.textProcedure.configure(state="disabled")
        self.buttonExecute.configure(state="disabled")
        self.comboboxALGOR.configure(state="disabled")

        return

    def enabledButtons(self, procedure):
        '''
        Function: This function is responsible for enabled specific frame components
        Inputs: Procedure Type
        Outputs:
        '''

        if procedure == 0:
            self.buttonSolution.configure(state="disabled")
            self.lblRestriction.configure(state="normal")
            self.textRestriction.configure(state="normal")
            self.buttonRestriction.configure(state="normal")
            self.entryRES.configure(state="normal")
        else:
            self.textProcedure.configure(state="normal")
            self.buttonExecute.configure(state="normal")
            self.comboboxALGOR.configure(state="normal")
        return

    def clearTextArea(self):
        self.textSolution.delete("1.0", "end")
        self.textRestriction.delete("1.0", "end")
        self.entryRES.delete(0, END)
        self.textProcedure.delete("1.0", "end")
        return

    def main(self):
        self.window.mainloop()
