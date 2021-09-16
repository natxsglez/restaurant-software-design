import sys
sys.path.append(".")

from Clases.Orden import Orden

class Mesa():
    def __init__(self, numMesa: int, orden: Orden) -> None:
        self.numMesa = numMesa
        self.orden = orden