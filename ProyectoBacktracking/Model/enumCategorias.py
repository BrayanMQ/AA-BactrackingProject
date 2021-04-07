# Imports
from enum import Enum


class Categorias(Enum):

    Sospechosos = ['El/la mejor amigo(a)', 'El/la novio(a)', 'El/la vecino(a)', 'El mensajero',
                   'El extraño', 'El/la hermanastro(a)', 'El/la colega de trabajo']
    Armas = ['Pistola', 'Cuchillo', 'Machete', 'Pala', 'Bate', 'Botella', 'Tubo', 'Cuerda']
    Motivos = ['Venganza', 'Celos', 'Dinero', 'Accidente', 'Drogas', 'Robo']
    PartesCuerpo = ['Cabeza', 'Pecho', 'Abdomen', 'Espalda', 'Piernas', 'Lugar']
    Lugares = ['Sala', 'Comedor', 'Baño', 'Terraza', 'Cuarto', 'Garage', 'Patio', 'Balcón']