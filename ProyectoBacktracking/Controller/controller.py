# IMPORTS
import View

# CLASSES
from View.MainWindow import Window


class Controller:

    def __init__(self):
        self.window = Window(self)

    def main(self):
        self.window.main()

    def hola(self):
        print('\nthis is a example')


if __name__ == '__main__':
    controller = Controller()
    controller.main()
