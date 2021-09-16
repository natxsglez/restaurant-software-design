
from Clases.Orden import Orden
from Clases.PlatoFuerte import PlatoFuerte
from Clases.Postre import Postre
from Clases.Entrada import Entrada
from Clases.Preparado import Preparado
from Clases.Refresco import Refresco

o1 = Orden([Postre(16.4,"Pastel"),PlatoFuerte(54,"Tacos")], [Preparado(50.5, "Margarita", "alcohol y más cosas", True), Refresco(45.6, "Coca")])
o1.agregarBebida(Refresco(20, "Pepsi"))
o1.agregarComida(Entrada(13.5, "Nachos"))
print("El total de la orden es:", o1.obtenerTotal())
print(o1)