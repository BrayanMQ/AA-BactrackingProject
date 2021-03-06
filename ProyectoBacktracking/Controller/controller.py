# IMPORTS
from View.MainWindow import Window
import random

# Import de los enums
from Model.enumCategories import Categories
from Model.Algorithm import Algorithm
from timeit import default_timer


# CLASSES
class Controller:

    def __init__(self):
        '''
        Constructor
        '''

        # Solution List
        self.solution = []

        # Restrictions List
        self.restrictions = []

        # Window Instance
        self.window = Window(self)

    def main(self):
        '''
        Function: This function is going to create a Window with all its characteristics
        Inputs:
        Outputs:
        '''
        self.window.main()

    def solutionFunction(self):
        '''
        Function: This function is going do a procedure when the solution button is clicked
        Inputs:
        Outputs:
        '''

        # This is going to enable some buttons until the solution button is clicked
        self.window.enabledButtons(0)

        # This create the solution
        self.createSolution()

        # This is going to create a string with the solution before created
        solutionString = ''
        for card in self.solution:
            solutionString += card + ', '

        # This is going to remove the last two characters
        solutionString = solutionString[:-2]

        # This is going to insert the solution to the solution text area
        self.window.textSolution.insert('insert', solutionString)

        return

    def restrictionFunction(self):
        '''
        Function: This function is going do a procedure when the restriction button is clicked
        Inputs:
        Outputs:
        '''

        # This is going to clear restriction list
        self.restrictions.clear()

        # This is going to enable some buttons until the restriction button is clicked
        self.window.enabledButtons(1)

        # This is going to clear the restriction text area
        self.window.textRestriction.delete("1.0", "end")

        # Number of restrictions (each restriction is a pair of cards)
        if self.window.entryRES.get() == "":
            self.window.showMessagesBox(1)
            return
        try:
            restrictionsAmount = int(self.window.entryRES.get())

            if restrictionsAmount > 15:
                self.window.showMessagesBox(3)
                return
            elif restrictionsAmount < 1:
                self.window.showMessagesBox(2)
                return
        except:
            self.window.showMessagesBox(2)
            return

        # Get reestrictions
        self.createRestrictions(restrictionsAmount)

        # This counter is to create the couples
        cont = 0

        # This counter is to create the string with a format order
        cont2 = 1

        # This is going to create a string with the solution before created
        restrictionString = str(cont2) + "-"
        for card in self.restrictions:

            # This is add the card and a comma to separate the restriction
            restrictionString += card + ', '
            cont += 1

            if cont == 2:
                cont = 0
                cont2 += 1

                # This is going to remove the last two characters
                restrictionString = restrictionString[:-2]

                # This is going add the counter and a symbol to the string
                restrictionString += "\n" + str(cont2) + "-"

        # This is going to remove the last count
        restrictionString = restrictionString[:-3]

        # This is going to insert the restriction to the restriction text area
        self.window.textRestriction.insert('insert', restrictionString)

        return

    def procedureFunction(self):
        '''
        Function: This function is going do a procedure when the procedure button is clicked
        Inputs:
        Outputs:
        '''

        #It clears textProcedure
        self.window.textProcedure.delete("1.0", "end")

        algorithm = None
        restrictionListAux = self.restrictions[:]

        # This is going to select algorithm type
        algorithmType = self.window.comboboxALGOR.get()
        if algorithmType == "Backtracking":
            algorithm = Algorithm(self.solution, restrictionListAux)
            print(algorithmType)

        elif algorithmType == "Brute Force":
            algorithm = Algorithm(self.solution, [])
            print(algorithmType)

        else:
            self.window.showMessagesBox(3)
            return

        # execute(0, len(solutionList)-1, [] , Categorias.listaCategories)

        # This is going to create a list of enum categories
        listCategories = []
        for category in Categories:
            listCategories2 = []
            for card in category.value:
                listCategories2.append(card)
            listCategories.append(listCategories2)

        # Begin of time
        begin = default_timer()

        value = algorithm.execute(0, len(self.solution), [], listCategories)

        # End of time
        end = default_timer()

        # This is going to set information of the procedure string to procedure text and execution time to execution
        # label
        self.window.textProcedure.insert("insert", value)
        self.window.lblTime.config(text="Tiempo de ejecuci??n: %f" % (end - begin) + " s")

        return

    def restoreFunction(self):
        '''
        Function: This function is going do a procedure when the restore button is clicked
        Inputs:
        Outputs:
        '''

        # This is going to clear the text area from window
        self.window.clearTextArea()

        # This is going to disable most buttons from window
        self.window.disabledButtons()

        # This is going to clean solution and restriction List
        self.solution.clear()
        self.restrictions.clear()


        return

    def createRestrictions(self, restrictionsAmount):
        '''
        Function: This function is going to create all the couple restrictions
        Inputs: Amount of restrictions
        Outputs:
        '''

        self.restrictions = []

        # Get restrictions
        i = 0
        while i < (restrictionsAmount * 2):

            # This is going to calculate a random number to get a random categorie
            randomCategory = random.choice(list(Categories))

            # This is going to calculate a random number to get a random card from the categorie
            randomNumber = random.randint(0, len(randomCategory.value) - 1)

            # If the selected card is not in the solution, then it adds it to the constraints
            # If not, go i-1 and search again

            if not randomCategory.value[randomNumber] in self.solution \
                    and not randomCategory.value[randomNumber] in self.restrictions:
                # Add the restriction
                self.restrictions.append(randomCategory.value[randomNumber])
                i += 1
        return

    def createSolution(self):

        self.solution = []

        # Get the solution
        for category in Categories:
            randomNumber = random.randint(0, len(category.value) - 1)

            # Add the card to the solution
            self.solution.append(category.value[randomNumber])


# This is going to create a controller and call main function
if __name__ == '__main__':
    controller = Controller()
    controller.main()
