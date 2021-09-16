import sys
sys.path.append("..")

from Clases.Menu import Menu
from abc import ABC

class Comida(ABC, Menu):
  def servir(self):
    pass