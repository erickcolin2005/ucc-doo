from datetime import datetime

# Clase Cuenta (Interfaz)
class Cuenta:
    def abrir_cuenta(self):
        pass

    def cerrar_cuenta(self):
        pass

    def consultar_saldo(self):
        pass

    def transferir_dinero(self, cuenta_destino, monto):
        pass


# Clase CuentaAhorro (Implementa Cuenta)
class CuentaAhorro(Cuenta):
    def __init__(self, id_cuenta, id_usuario, tipo_cuenta, saldo, estado, fecha_apertura):
        self.id_cuenta = id_cuenta
        self.id_usuario = id_usuario
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.estado = estado
        self.fecha_apertura = fecha_apertura

    def abrir_cuenta(self):
        self.estado = "Abierta"
        self.fecha_apertura = datetime.now()
        print(f"Cuenta {self.id_cuenta} abierta exitosamente.")

    def cerrar_cuenta(self):
        if self.saldo == 0:
            self.estado = "Cerrada"
            print(f"Cuenta {self.id_cuenta} cerrada exitosamente.")
        else:
            print("La cuenta no puede cerrarse, tiene saldo pendiente.")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta {self.id_cuenta} es: {self.saldo}")

    def transferir_dinero(self, cuenta_destino, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            cuenta_destino.saldo += monto
            print(f"Transferencia de {monto} realizada con éxito a la cuenta {cuenta_destino.id_cuenta}.")
        else:
            print("Saldo insuficiente para realizar la transferencia.")


# Clase Usuario (Interfaz)
class Usuario:
    def registrar_usuario(self):
        pass

    def actualizar_datos(self):
        pass


# Clase Cliente (Implementa Usuario)
class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, apellido, correo, telefono, direccion, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.rol = rol

    def registrar_usuario(self):
        print(f"Usuario {self.nombre} {self.apellido} registrado exitosamente.")

    def actualizar_datos(self, nombre=None, apellido=None, correo=None, telefono=None, direccion=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if correo:
            self.correo = correo
        if telefono:
            self.telefono = telefono
        if direccion:
            self.direccion = direccion
        print(f"Datos del usuario {self.id_usuario} actualizados con éxito.")


# Clase Transacción (Interfaz)
class Transaccion:
    def realizar_transaccion(self):
        pass


# Clase Transferencia (Implementa Transacción)
class Transferencia(Transaccion):
    def __init__(self, id_transaccion, id_cuenta_origen, id_cuenta_destino, monto, tipo_transaccion, fecha_transaccion):
        self.id_transaccion = id_transaccion
        self.id_cuenta_origen = id_cuenta_origen
        self.id_cuenta_destino = id_cuenta_destino
        self.monto = monto
        self.tipo_transaccion = tipo_transaccion
        self.fecha_transaccion = fecha_transaccion

    def realizar_transaccion(self):
        print(f"Transacción {self.id_transaccion} realizada con éxito.")


# Clase Prestamo (Interfaz)
class Prestamo:
    def solicitar_prestamo(self):
        pass

    def aprobar_prestamo(self):
        pass


# Clase PrestamoPersonal (Implementa Prestamo)
class PrestamoPersonal(Prestamo):
    def __init__(self, id_prestamo, id_usuario, monto, plazo, estado, fecha_solicitud):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.monto = monto
        self.plazo = plazo
        self.estado = estado
        self.fecha_solicitud = fecha_solicitud

    def solicitar_prestamo(self):
        self.estado = "Pendiente"
        self.fecha_solicitud = datetime.now()
        print(f"Préstamo {self.id_prestamo} solicitado por el usuario {self.id_usuario}.")

    def aprobar_prestamo(self):
        self.estado = "Aprobado"
        print(f"Préstamo {self.id_prestamo} aprobado exitosamente.")
 