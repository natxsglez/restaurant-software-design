import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class PlatoFuerte(Comida):
  def __str__(self):
    return 'Clase plato fuerte'

  def servir(self):
    return 'Sirviendo plato fuerte'
