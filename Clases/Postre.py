import sys
sys.path.append("..")

from Interfaces.Comida import Comida

class Postre(Comida):
  def __str__(self):
    return 'Clase postre'

  def servir(self):
    return 'Sirviendo postre'
