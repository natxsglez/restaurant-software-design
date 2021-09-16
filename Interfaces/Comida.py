import sys
sys.path.append("..")

from Clases.Menu import Menu
from abc import ABC

class Comida(ABC, Menu):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Asigna un precio y un nombre a una comida '''
    super().__init__(precio, nombre)

  def servir(self) -> None:
    ''' Sirve la comida lista '''
    print(f"El alimento {self.nombre} se ha servido!")