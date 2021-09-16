import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class Entrada(Comida):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Asigna un precio y un nombre a una entrada de comida '''
    super().__init__(precio, nombre)

  def __str__(self) -> str:
    ''' Devuelve el nombre y el tipo de alimento '''
    return f'La comida {self.nombre} es una entrada'

  def servir(self) -> None:
    ''' Sirve la comida lista '''
    print(f"La entrada {self.nombre} se ha servido!")
