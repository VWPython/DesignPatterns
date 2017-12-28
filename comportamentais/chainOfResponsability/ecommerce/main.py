from calculador import Calculador
from carrinho import Carrinho
from item import Item

compra = Carrinho()
compra.adiciona_item(Item('item01', 100))
compra.adiciona_item(Item('item02', 100))
compra.adiciona_item(Item('item03', 100))
compra.adiciona_item(Item('item04', 100))
compra.adiciona_item(Item('item05', 100))

print(compra.valor_total)

calculador = Calculador()

desconto = calculador.calcula(compra)

print('Desconto:', desconto)
