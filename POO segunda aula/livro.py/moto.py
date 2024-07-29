class Moto:
    def __init__(self, marca, modelo, cilindradas):
     self.marca = marca
     self.modelo = modelo
     self.cilindradas = cilindradas 

Moto1 = Moto("Honda", "2018 Honda CRF250R", 249 )
print("A moto {} da marca {} possui {} cilindradas".format(Moto1.modelo, Moto1.marca, Moto1.cilindradas) )

Moto2 = Moto("Yamaha", "Yamaha XJ6", 600 )
print("A moto {} da marca {} possui {} cilindradas".format(Moto2.modelo, Moto2.marca, Moto2.cilindradas) )      