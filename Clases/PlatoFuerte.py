import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class PlatoFuerte(Comida):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Asigna un precio y un nombre a un plato fuerte de comida '''
    super().__init__(precio, nombre)

  def __str__(self) -> str:
    ''' Devuelve el nombre y el tipo de alimento '''
    return f'La comida {self.nombre} es un plato fuerte'

  def servir(self) -> None:
    ''' Sirve la comida lista '''
    print(f"El plato fuerte {self.nombre} se ha servido!")
