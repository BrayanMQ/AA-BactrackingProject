# IMPORTS
import View
from View.MainWindow import Window
import random

# Import de los enums
from Model.EnumSospechosos import Sospechosos
from Model.EnumArmas import Armas
from Model.EnumMotivos import Motivos
from Model.EnumPartesCuerpo import PartesCuerpo
from Model.EnumLugares import Lugares


# CLASSES
class Controller:

    def __init__(self):
        '''
        Constructor
        '''

        # Lista que contiene las categorías
        self.categoryList = [Sospechosos, Armas, Motivos, PartesCuerpo, Lugares]

        # Lista que guarda la solución
        self.solution = []

        # Lista que guarda las restricciones
        self.restrictions = []

        self.window = Window(self)

    def main(self):
        '''
        Function: This function is going to create a Window with all its characteristics
        Inputs:
        Outputs:
        '''
        self.window.main()

    def createSolution(self):
        # Obtiene la solución
        for category in self.categoryList:

            randomNumber = random.randint(1, len(category))

            # Agrega la carta a la solución
            self.solution.append(category(randomNumber).name)

    def solutionFunction(self):
        '''
        Function: This function is going do a procedure when the solution button is clicked
        Inputs:
        Outputs:
        '''
        self.window.enabledButtons(0)

        #Crea la solución
        self.createSolution()

        solutionString = ''
        for card in self.solution:

            solutionString += card + ', '

        solutionString = solutionString[:-2]
        self.window.textSolution.insert('insert', solutionString)

        # if self.window.textSolution.get("1.0") is not None:
        #    self.window.textSolution.delete("1.0", "end")
        # self.window.textSolution.insert('insert',"This is a example   "+str(self.cont))
        # self.window.textRestriction.insert('insert', "This is a example")

        return

    def createRestrictions(self, restrictionsAmount):

        # Obtener restricciones
        i = 0
        while i < (restrictionsAmount * 2):

            # Calcula el número random para obtener una categoría random
            randomNumber = random.randint(0, 4)
            randomCategory = self.categoryList[randomNumber]

            # Calcula el número random para obtener una carta de la categoría
            randomNumber = random.randint(1, len(randomCategory))

            # Si la carta seleccionada no está en la solución, entonces la agrega a las restricciones
            # Sino, hace i-1 y busca de nuevo
            if not randomCategory(randomNumber).name in self.solution \
                    and not randomCategory(randomNumber).name in self.restrictions:
                # Agrega la restricción
                self.restrictions.append(randomCategory(randomNumber).name)
                i += 1
        return


    def restrictionFunction(self):
        '''
        Function: This function is going do a procedure when the restriction button is clicked
        Inputs:
        Outputs:
        '''

        self.restrictions.clear()
        self.window.textRestriction.delete("1.0", "end")

        # Cantidad restricciones (cada restricción es un par de cartas)
        if self.window.entryRES.get() is not None:
            restrictionsAmount = int(self.window.entryRES.get())

        # Obtiene las restricciones
        self.createRestrictions(restrictionsAmount)

        restrictionString = ''
        for card in self.restrictions:

            restrictionString += card + ', '

        restrictionString = restrictionString[:-2]
        self.window.textRestriction.insert('insert', restrictionString)

        return

    def procedureFunction(self):
        '''
        Function: This function is going do a procedure when the procedure button is clicked
        Inputs:
        Outputs:
        '''
        print("Procedure function")
        return

    def restoreFunction(self):
        '''
        Function: This function is going do a procedure when the restore button is clicked
        Inputs:
        Outputs:
        '''
        self.window.disabledButtons()

        # Limpia la solución y las restricciones
        self.solution.clear()
        self.restrictions.clear()
        return

if __name__ == '__main__':
    controller = Controller()
    controller.main()
