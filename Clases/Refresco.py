from Interfaces.Bebida import Bebida


class Refresco(Bebida):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Crea una instancia de un refresco '''
    super().__init__(precio, nombre)

  def __str__(self) -> str:
    ''' Devuelve el nombre y el tipo de bebida '''
    return f'La bebida {self.nombre} es un refresco'
