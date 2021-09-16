from Interfaces.Bebida import Bebida


class Refresco(Bebida):
    def __init__(self, precio: float, nombre: str) -> None:
        super().__init__(precio, 'Refresco' + nombre)

    def __str__(self):
        return self.nombre
