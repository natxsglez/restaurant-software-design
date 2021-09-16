import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class Postre(Comida):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Asigna un precio y un nombre a un postre de comida '''
    super().__init__(precio, nombre)

  def __str__(self) -> str:
    ''' Devuelve el nombre y el tipo de alimento '''
    return f'La comida {self.nombre} es un postre'

  def servir(self) -> None:
    ''' Sirve la comida lista '''
    print(f"El postre {self.nombre} se ha servido!")
