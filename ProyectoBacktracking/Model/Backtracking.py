
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
        self.cont = 0

    # i = 0, n = Tamaño de la solucion,  categoria = Lista de valores de una categoria
    # execute(0, len(solutionList)-1, [] , Categorias.listaCategories)

    def execute(self, i, n, listaAuxSolution, listCategories):

        if i == n:
            print(str(self.cont), listaAuxSolution)
            self.cont += 1
            # Crea el string
            for card in listaAuxSolution:
                self.stringResult += str(card) + ", "

            #self.stringResult[:-2]

            if self.sameSolution(listaAuxSolution):
                self.stringResult += " | Solución Correcta\n"
                self.solutionFound = True
            else:
                self.stringResult += " | Solución Incorrecta\n"
                # restriccion de la carta
                #
                #

        else:

            # Recorre las categorias
            for j in range(i, n):

                # Recorre los elementos de una categoria
                for w in range(0, len(listCategories[j])):

                    listaAuxSolution.append(listCategories[j][w])

                    self.stringResult = self.execute(i + 1, n, listaAuxSolution, listCategories)

                    #bandera
                    if self.solutionFound:
                        return self.stringResult

                    listaAuxSolution.pop()

                break

        return self.stringResult

    def sameSolution(self, lista):
        for i in range(len(self.solutionList)):
            if self.solutionList[i] != lista[i]:
                return False
        return True
