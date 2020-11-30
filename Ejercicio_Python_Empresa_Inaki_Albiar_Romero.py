class Empleado:
    def __init__(self, nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl):
        self.nombreEmpl=nombreEmpl
        self.apellidoEmpl=apellidoEmpl
        self.dniEmpl=dniEmpl
        self.direccionEmpl=direccionEmpl
        self.antiguedadEmpl=antiguedadEmpl
        self.telefonoEmpl=telefonoEmpl
        self.salarioEmpl=salarioEmpl
    def imprimir(self):
        print("Nombre del Empleado: ", self.nombreEmpl , " Apellido del Empleado: " , self.apellidoEmpl , " DNI del Empleado: " , self.dniEmpl ,
              " Dirección donde vive el Empleado: " , self.direccionEmpl , " Antigüedad del Empleado en la Empresa: " , self.antiguedadEmpl ,
              "Telefono de contacto del Empleado: " , self.telefonoEmpl , "Salario del Empleado: " , self.salarioEmpl)
    def cambiarSupervisor(self, supervisor):
        self.supervisor=supervisor
        print("El nuevo supervisor es: ", supervisor)
    def incrementarSalario(self, incremento):
        self.salarioEmpl= (self.salarioEmpl * incremento)/100 + self.salarioEmpl
        print("El salario incrementado es: ", self.salario)
Primerempleadoempresa=Empleado("Carlos","Loma","11122332S","Calle San Juan De Dios",6,789456123,1990)
empleado2=Empleado("Carla","Seda","456217665A","Calle Recogidas",8,123456789,2500)
empleado1.imprimir()
empleado1.incrementarSalario(6)
print("EL PROGRAMA HA LLEGADO A SU FIN")

class Secretario(Empleado):
    def __init__(self,nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl, faxSec, despachoSec, puestoSec):
        Empleado.__init__(self,nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl)
        self.faxSec=faxSec
        self.despachoSec=despachoSec
        self.puestoSec=puestoSec

    def incrementarSalario(self):
        super(Secretario, self).incrementarSalario(2)

    def imprimir(self):
        super(Secretario, self).imprimir()
        print("Puesto en la empresa: " + str(self.puesto))
secretario1=Secretario("Juan Manuel","Lopez","321654987D","Avenida San Matías",8,123654712,2900, "753215987","Q3","Secretario")
secretario2=Secretario("Maria","Suarez","78541236F","Carretera de Jaen",2,123789412,4500, "123658716","Q4","Secretaria")
secretario1.imprimir()
secretario2.imprimir()
print(
    "El fax del secretario ", secretario1.nombre, " es: ", secretario1.fax,
    "El despacho de secretario ", secretario1.nombre, " es el: ", secretario1.despacho,
    "Su puesto en la empresa es ", secretario1.puesto)
print(
    "El fax del secretario ", secretario2.nombre, " es: ", secretario2.fax,
    "El despacho de secretario ", secretario2.nombre, " es el: ", secretario2.despacho,
    "Su puesto en la empresa es ", secretario2.puesto)
secretario1.incrementarSalario()
secretario2.incrementarSalario()

print("FIN")

class Coche:
    def __init__(self,matricula, marca, modelo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo

coche1 = Coche("1236547Q","Lamborghini","URUS")
coche2 = Coche("3698521Y","FORD","MUSTANG MACH-E")
coche3 = Coche("7894561L","SEAT","LEÓN FR")



listaClientes = ["Juan","Manuel","Michael"]
class Vendedor(Empleado):
    def __init__(self, nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl, coche2, area, comision, listaClientes ):
        Empleado.__init__(self, nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl)
        self.coche = coche2
        self.area=area
        self.comision=comision
        self.listaClientes=listaClientes
    def alta(self, nombre):
        self.listaClientes.append(nombreEmpl)
    def baja(self, nombreEmpl):
        self.listaClientes.remove(nombreEmpl)
    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)
    def incrementarSalario(self):
        super(Vendedor, self).incrementarSalario(10)

listaVendedores=["Carlos","Antonio","Diego"]
vendedor1=Vendedor("Leo","Siles","65465456R","Carretera de Mlaga",8,7511551,2250, coche1, "Ventas", 4, listaClientes)
vendedor1.imprimir()
print(
    "Marcar de coche: ", vendedor1.coche.marca,
    "Area de trabajo: ", vendedor1.area,
    "Comisión: ", vendedor1.comision,
    "Lista de clientes: ", vendedor1.listaClientes)
vendedor1.incrementarSalario()
print("FIN")


class Jefe(Empleado):
    def __init__(self, nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl, secretario1, coche3, despacho, listaVendedores ):
        Empleado.__init__(self, nombreEmpl, apellidoEmpl, dniEmpl, direccionEmpl, antiguedadEmpl, telefonoEmpl, salarioEmpl)
        self.secretario=secretario1
        self.coche=coche3
        self.despacho=despacho
        self.listaVendedores=listaVendedores
    def incrementarSalario(self):
        super(Jefe, self).incrementarSalario(20)
    def cambiarSecretario(self, secretario):
        self.secretario=secretario
        print("El nuevo secretario es: ", secretario.nombre)
    def cambiarCoche(self, coche):
        self.coche=coche
        print("El nuevo coche es: ", coche.marca)
    def altaVendedor(self, nombreEmpl):
        self.listaVendedores.append(nombreEmpl)
    def bajaVendedor(self, nombreEmpl):
        self.listaVendedores.remove(nombreEmpl)

jefe1=Jefe("Juan","Ordoñez","59358702F","Calle Granada",3,349093748,4000,secretario1,coche2,"Direccion",listaVendedores)
jefe1.imprimir()
print(
    "Secretario: ", jefe1.secretario.nombre,
    "Marca coche: ", jefe1.coche.marca,
    "Despacho: ", jefe1.despacho,
    "Lista de vendedores: ", jefe1.listaVendedores)
jefe1.incrementarSalario()
print("FIN")
