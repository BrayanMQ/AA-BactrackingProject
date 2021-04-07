# IMPORTS
import View
from View.MainWindow import Window
import random

# Import de los enums
from Model.enumCategorias import Categorias

# CLASSES
class Controller:

    def __init__(self):
        '''
        Constructor
        '''

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
        for category in Categorias:

            randomNumber = random.randint(0, len(category.value) - 1)

            # Agrega la carta a la solución
            self.solution.append(category.value[randomNumber])

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
            randomCategory = random.choice(list(Categorias))

            # Calcula el número random para obtener una carta de la categoría
            randomNumber = random.randint(0, len(randomCategory.value) - 1)

            # Si la carta seleccionada no está en la sol ución, entonces la agrega a las restricciones
            # Sino, hace i-1 y busca de nuevo
            if not randomCategory.value[randomNumber] in self.solution \
                    and not randomCategory.value[randomNumber] in self.restrictions:
                # Agrega la restricción
                self.restrictions.append(randomCategory.value[randomNumber])
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
