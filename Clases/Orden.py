from Interfaces.Comida import Comida
from Interfaces.Bebida import Bebida

class Orden():
  siguienteOrden = 1

  def __init__(self, comidas: list, bebidas: list) -> None:
    ''' Permite añadir inicialmente una serie alimentos y bebidas a la orden '''
    self._comidas = comidas
    self._bebidas = bebidas
    self._numeroDeOrden = Orden.siguienteOrden
    Orden.siguienteOrden = Orden.siguienteOrden + 1

  def agregarComida(self, comida: Comida) -> bool:
    ''' Permite agregar un alimento a la orden '''
    if(not isinstance(comida,Comida)):
      return False
    self._comidas.append(comida)
    print(f"Se agregó {comida.nombre} a la orden correctamente")
    return True

  def agregarBebida(self, bebida: Bebida) -> bool:
    ''' Permite agregar una bebida a la orden '''
    if(not isinstance(bebida, Bebida)):
      return False
    self._bebidas.append(bebida)
    print(f"Se agregó {bebida.nombre} a la orden correctamente")
    return True

  def obtenerTotal(self) -> float:
    ''' Obtiene el total de la cuenta de la orden'''
    total = 0.0
    for comida in self._comidas:
      total = total + comida.precio
    for bebida in self._bebidas:
      total = total + bebida.precio
    return total

  def __str__(self) -> str:
    ''' Regresa los detalles de la orden'''
    ordenStr = f"Orden número {self._numeroDeOrden} con un total de {self.obtenerTotal()}\n"
    comidasStr = ""
    for comida in self._comidas:
      comidasStr = comidasStr + comida.nombre + ", "
    bebidasStr = ""
    for bebida in self._bebidas:
      bebidasStr = bebidasStr + bebida.nombre + ", "
    ordenStr = ordenStr + "\tDetalle comidas: " + comidasStr[:-2] + "\n"
    ordenStr = ordenStr + "\tDetalle bebidas: " + bebidasStr[:-2]
    return ordenStr