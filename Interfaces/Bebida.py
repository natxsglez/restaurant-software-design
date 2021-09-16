from Clases.Menu import Menu


class Bebida(Menu):
  def __init__(self, precio: float, nombre: str) -> None:
    ''' Asigna un precio y un nombre a una bebida '''
    super().__init__(precio, nombre)

  def refill(self):
    ''' Hace un refill de la bebida '''
    print('Se hizo un refill a ' + self.nombre)
