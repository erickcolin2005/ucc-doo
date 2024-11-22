class Vuelo:
    def __init__(self, id_vuelo, origen, destino, fecha, hora, precio, aerolinea):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.precio = precio
        self.aerolinea = aerolinea

    @staticmethod
    def buscar_vuelos(vuelos, origen=None, destino=None):
        resultados = [vuelo for vuelo in vuelos if
                      (origen is None or vuelo.origen == origen) and
                      (destino is None or vuelo.destino == destino)]
        return resultados
    


class Pasajero:
    def __init__(self, id_pasajero, nombre, apellido, email, telefono, fecha_nacimiento):
        self.id_pasajero = id_pasajero
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def registrar(self, pasajeros):
        pasajeros.append(self)
        return f"Pasajero {self.nombre} {self.apellido} registrado exitosamente."


class Reserva:
    def __init__(self, id_reserva, pasajero, vuelo, fecha_reserva, estado):
        self.id_reserva = id_reserva
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva
        self.estado = estado

    @staticmethod
    def crear_reserva(reservas, pasajero, vuelo, fecha_reserva):
        nueva_reserva = Reserva(len(reservas) + 1, pasajero, vuelo, fecha_reserva, "Confirmada")
        reservas.append(nueva_reserva)
        return nueva_reserva


class Pago:
    def __init__(self, id_pago, reserva, monto, fecha_pago, metodo_pago):
        self.id_pago = id_pago
        self.reserva = reserva
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago

    @staticmethod
    def realizar_pago(pagos, reserva, monto, metodo_pago):
        nuevo_pago = Pago(len(pagos) + 1, reserva, monto, "2024-11-22", metodo_pago)
        pagos.append(nuevo_pago)
        return nuevo_pago


class Notificacion:
    def __init__(self, id_notificacion, reserva, mensaje, fecha_envio, estado):
        self.id_notificacion = id_notificacion
        self.reserva = reserva
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio
        self.estado = estado

    @staticmethod
    def enviar_notificacion(notificaciones, reserva, mensaje):
        nueva_notificacion = Notificacion(len(notificaciones) + 1, reserva, mensaje, "2024-11-22", "Enviada")
        notificaciones.append(nueva_notificacion)
        return nueva_notificacion


# Ejemplo de uso

# Listas para simular bases de datos
vuelos = [
    Vuelo(1, "Bogotá", "Medellín", "2024-12-01", "10:00", 150.00, "Avianca"),
    Vuelo(2, "Cali", "Cartagena", "2024-12-02", "15:30", 200.00, "LATAM"),
]
pasajeros = []
reservas = []
pagos = []
notificaciones = []

# Registro de pasajero
juan = Pasajero(1, "Juan", "Pérez", "juan.perez@example.com", "3001234567", "1990-05-20")
print(juan.registrar(pasajeros))

# Búsqueda de vuelos
resultados = Vuelo.buscar_vuelos(vuelos, origen="Bogotá")
for vuelo in resultados:
    print(f"Vuelo encontrado: {vuelo.origen} -> {vuelo.destino}, Precio: {vuelo.precio}")

# Creación de reserva
reserva = Reserva.crear_reserva(reservas, juan, vuelos[0], "2024-11-20")
print(f"Reserva creada para {reserva.pasajero.nombre} en el vuelo {reserva.vuelo.origen} -> {reserva.vuelo.destino}")

# Realización de pago
pago = Pago.realizar_pago(pagos, reserva, 150.00, "Tarjeta de Crédito")
print(f"Pago realizado: {pago.monto} con {pago.metodo_pago}")

# Envío de notificación
notificacion = Notificacion.enviar_notificacion(notificaciones, reserva, "Su vuelo ha sido confirmado.")
print(f"Notificación enviada: {notificacion.mensaje}")
