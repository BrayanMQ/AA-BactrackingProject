# Imports
from enum import Enum


# This is the categories Enum
class Categories(Enum):
    Sospechosos = ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero',
                   'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo']
    Armas = ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo', 'Cuerda']
    Motivos = ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo']
    PartesCuerpo = ['Cabeza', 'Pecho', 'Abdomen', 'Espalda', 'Piernas', 'Brazos']
    Lugares = ['Sala', 'Comedor', 'Baño', 'Terraza', 'Cuarto', 'Garage', 'Patio', 'Balcón', 'Cocina']

    def listCategories(self):
        return self.value
