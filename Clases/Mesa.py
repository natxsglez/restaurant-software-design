import sys
sys.path.append(".")

from Clases.Orden import Orden

class Mesa():
  def __init__(self, numMesa: int, orden: Orden) -> None:
    ''' Se crea el registro de una mesa y se asigna una orden a la misma '''
    self.numMesa = numMesa
    self.orden = orden

  def obtenerCuenta(self) -> None:
    ''' Obtiene la cuenta de la mesa '''
    print(f'El total de la cuenta es: ${self.orden.obtenerTotal()}')