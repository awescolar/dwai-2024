class Veiculo:
    def __init__(self, fabricante, modelo, ano):
     self.fabricante = fabricante
     self.modelo = modelo
     self.ano = ano

Carro1 = Veiculo("Chevrolet", "Chevrolet Onix", 2022)
print("A fabricante {} fabricou o {} em {}".format(Carro1.fabricante, Carro1.modelo, Carro1.ano) )

Carro2 = Veiculo("Fiat", "Fiat uno 2010", 2010)
print("A fabricante {} fabricou o {} em {}".format(Carro2.fabricante, Carro2.modelo, Carro2.ano) )