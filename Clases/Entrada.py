import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class Entrada(Comida):
  def __str__(self):
    return 'Clase entrada'

  def servir(self):
    return 'Sirviendo entrada'
