from Interfaces.Bebida import Bebida


class Preparado(Bebida):
  def __init__(self, precio: float, nombre: str, ingredientes: str, tieneAlcohol: bool) -> None:
    ''' Crea una instancia de una bebida preparada '''
    super().__init__(precio, nombre)
    self.ingredientes = ingredientes.split(',')
    self.tieneAlcohol = tieneAlcohol

  def __str__(self) -> str:
    ''' Devuelve el nombre y el tipo de bebida '''
    return f'La bebida {self.nombre} es un preparado'

  def agregarIngrediente(self, ingrediente: str) -> None:
    ''' Agrega un ingrediente al arreglo de ingredientes de la bebida preparada '''
    self.ingredientes.append(ingrediente)
