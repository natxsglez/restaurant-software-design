
from Clases.Orden import Orden
from Clases.PlatoFuerte import PlatoFuerte
from Clases.Postre import Postre
from Clases.Entrada import Entrada
from Clases.Preparado import Preparado
from Clases.Refresco import Refresco
from Clases.Mesa import Mesa

o1 = Orden([Postre(16.4,"Pastel"),PlatoFuerte(54,"Tacos")], [Preparado(50.5, "Margarita", "alcohol y más cosas", True), Refresco(45.6, "Coca")])
m1 = Mesa(1, o1)
o1.agregarBebida(Refresco(20, "Pepsi"))
o1.agregarComida(Entrada(13.5, "Nachos"))
m1.obtenerCuenta()