import random


# Class
class Backtracking:

    def __init__(self, sList, rList):
        '''
            Constructor
        '''

        self.solutionList = sList
        self.restrictionList = rList
        self.solutionFound = False
        self.stringResult = ""
        self.restrictionAdded = False
        self.cont = 0

    def sameSolution(self, lista):
        for i in range(len(self.solutionList)):
            if self.solutionList[i] != lista[i]:
                return False
        return True

    # i = 0,
    # n = size of solution
    def execute(self, i, n, listAuxSolution, CategoriesList):

        if i == n:

            # It creates the string
            for card in listAuxSolution:
                self.stringResult += str(card) + ", "

            self.stringResult = self.stringResult[:-2]

            # If both solutions are the same
            if self.sameSolution(listAuxSolution):
                self.stringResult += " | Solución Correcta\n"
                self.solutionFound = True
            else:
                self.stringResult += " | Solución Incorrecta"

                # It selects a restriction card
                auxList = listAuxSolution[:]

                # While auxList not empty
                while not len(auxList) == 0:
                    card = random.choice(auxList)

                    # If selected card isn't in solution or restriction list, then it adds it to restrictions
                    if card not in self.solutionList and card not in self.restrictionList:

                        self.restrictionList.append(card)
                        self.stringResult += " | Nueva restricción: " + card + "\n"

                        # Flag used for knowing if a restriction card was add
                        self.restrictionAdded = True
                        break

                    else:
                        # Else, it removes card from auxList
                        auxList.remove(card)

                # If flag is not on means that algorithm could not add a restriction
                if not self.restrictionAdded:
                    self.stringResult += " | No se agregó restricción.\n"
                else:
                    self.restrictionAdded = False

            return self.stringResult

        else:

            # It goes through the categories
            for j in range(i, n):

                # It goes through category elements
                for w in range(0, len(CategoriesList[j])):

                    # If card not in restriction list, the it adds it to listaAuxSolution
                    if not CategoriesList[j][w] in self.restrictionList:

                        listAuxSolution.append(CategoriesList[j][w])

                        self.stringResult = self.execute(i + 1, n, listAuxSolution, CategoriesList)

                        # Flag
                        if self.solutionFound:
                            return self.stringResult

                        listAuxSolution.pop()

                break

        return self.stringResult
