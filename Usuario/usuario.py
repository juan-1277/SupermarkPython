from personas import *
class UsuarioAdmin(Persona):
    def __init__(self, clave, usuarioAdmin=[]):
        self.__clave = clave
        
@property
def clave(self):
        return self.__clave
    
@clave.setter
def clave(self,clave):
        self.__clave = clave

def __str__(self):
        return f"{self.__nombre} {self.__apellido} {self.__domicilio} {self.__dni} {self._clave}"
        

class UsuarioCliente(Persona):
    def __init__(self, email, condFiscal, usuarioCliente=[]):
        self.__email = email
        self.__condFiscal = condFiscal
        
@property
def email(self):
        return self.__email
    
@email.setter
def email(self,email):
        self.__email = email

@property
def condFiscal(self):
        return self.__condFiscal
    
@condFiscal.setter
def condFiscal(self,condFiscal):
        self.__condFiscal = condFiscal
        
def crear_usuarioAdmin(self):
    nombre = input("Ingrese el nombre del Usuario ➡️ ")
    apellido = input("Ingrese el apellido del Usuario ➡️ ")
    domicilio = input("Ingrese el domicilio ➡️ ")
    dni = input("Ingrese el DNI del Usuario ➡️ ")
    clave = input("Ingrese la clave ➡️ ")
        
    usuario = UsuarioAdmin(nombre,apellido,domicilio,dni,clave)
    self.__usuarioAdmin.append(usuario)
        
def crear_usuarioCliente(self):
    nombre = input("Ingrese su nombre ➡️ ")
    apellido = input("Ingrese su apellido ➡️ ")
    domicilio = input("Ingrese su domicilio ➡️ ")
    dni = input("Ingrese su DNI ➡️ ")
    email= input("Ingrese su email ➡️ ")
    condFiscal = input("Ingrese su Condicion Fiscal ➡️ ")
        
    cliente = UsuarioCliente(nombre,apellido,domicilio,dni,email,condFiscal)
    self.__usuarioCliente.append(cliente)