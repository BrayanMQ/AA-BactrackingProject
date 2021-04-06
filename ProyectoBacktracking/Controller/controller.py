# IMPORTS
import View
from View.MainWindow import Window

# CLASSES
class Controller:

    def __init__(self):
        '''
        Constructor
        '''
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
        print("Solution function")
        self.window.enabledButtons(0)
        #if self.window.textSolution.get("1.0") is not None:
        #    self.window.textSolution.delete("1.0", "end")
        #self.window.textSolution.insert('insert',"This is a example   "+str(self.cont))
        #self.window.textRestriction.insert('insert', "This is a example")
        return

    def restrictionFunction(self):
        '''
        Function: This function is going do a procedure when the restriction button is clicked
        Inputs:
        Outputs:
        '''
        print("Restriction function")
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
        return

if __name__ == '__main__':
    controller = Controller()
    controller.main()
