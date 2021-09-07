#Clase es un modelo con atributos y metodos.
class Empresa:
    def __init__(self,nom='El mas barato',ruc='0999999999',tel='042971234',dir='Juan Montalvo y Pedro Carbo'): #con atributos; son variables locales
         self.nombre=nom#que atributos requiere
         self.ruc=ruc
         self.telefono=tel
         self.direccion=dir
    def mostrarEmpresa(self):
        print('Empresa: {:20} RuC:{}'.format(self.nombre,self.ruc))
class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel

    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente): #Aplicando herencia
    def __init__(self,nom,ced,tel,contrato):
        super().__init__(nom,ced,tel)
        self.__contrato = contrato  # atributo privado representado con __
    @property
    def contrato(self):#getter: obetener el valor del aributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self,value): #setter: cambiar el valor del atributo privado
        if value:
            self.__contrato=value
        else:
            self.__contrato = 'Sin contrato'

    def mostrarCliente(self):
        print(self.nombre,self.__contrato) #Poliformismo: llamar al mismo metodo pero cambiar su comportamiento, prevalece la clase que se llama.

class ClientePersonal(Cliente): #Aplicando herencia
    def __init__(self,nom,ced,tel,promocion=True):
        super().__init__(nom,ced,tel)
        self.__promocion = promocion
    @property
    def promocion(self):
        if self.__promocion==True:
            return '10% de Descuento'
        else:
            return 'No hay Promocion'

    def mostrarCliente(self):
        print(self.nombre,self.promocion)

#emp=Empresa()
#emp.mostrarEmpresa()#instanciando el cobjeto
#print(emp.nombre)

cli1=ClientePersonal('Jose','0912231499','04256789',True)
cli1.mostrarCliente()