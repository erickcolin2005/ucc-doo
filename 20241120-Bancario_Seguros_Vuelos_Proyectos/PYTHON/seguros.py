from datetime import datetime

# Clase Cliente
class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def mostrar_informacion(self):
        return f"Cliente {self.id_cliente}: {self.nombre} {self.apellido}, {self.correo}"

# Clase Póliza
class Poliza:
    def __init__(self, id_poliza, cliente, tipo_poliza, monto_cobertura, prima, fecha_inicio, fecha_fin, estado):
        self.id_poliza = id_poliza
        self.cliente = cliente  # Relación con Cliente
        self.tipo_poliza = tipo_poliza
        self.monto_cobertura = monto_cobertura
        self.prima = prima
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado

    def renovar_poliza(self, nueva_fecha_fin):
        self.fecha_fin = nueva_fecha_fin
        self.estado = "Renovada"

# Clase Reclamación
class Reclamacion:
    def __init__(self, id_reclamacion, poliza, descripcion, monto_reclamado, estado):
        self.id_reclamacion = id_reclamacion
        self.poliza = poliza  # Relación con Poliza
        self.descripcion = descripcion
        self.monto_reclamado = monto_reclamado
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

# Clase Pago
class Pago:
    def __init__(self, id_pago, poliza, monto, metodo_pago, fecha_pago=None):
        self.id_pago = id_pago
        self.poliza = poliza  # Relación con Poliza
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.fecha_pago = fecha_pago or datetime.now()

# Clase Evaluación de Riesgo
class EvaluacionRiesgo:
    def __init__(self, id_evaluacion, reclamacion, nivel_riesgo, comentarios):
        self.id_evaluacion = id_evaluacion
        self.reclamacion = reclamacion  # Relación con Reclamacion
        self.nivel_riesgo = nivel_riesgo
        self.comentarios = comentarios

# Ejemplo de Uso
if __name__ == "__main__":
    # Crear cliente
    cliente1 = Cliente(1, "Juan", "Pérez", "juan.perez@email.com", "1234567890", "Calle Falsa 123")
    print(cliente1.mostrar_informacion())

    # Crear póliza
    poliza1 = Poliza(1, cliente1, "Auto", 100000.00, 5000.00, "2024-01-01", "2025-01-01", "Activa")
    print(f"Póliza {poliza1.id_poliza}: Tipo: {poliza1.tipo_poliza}, Estado: {poliza1.estado}")

    # Crear reclamación
    reclamacion1 = Reclamacion(1, poliza1, "Accidente de tránsito", 15000.00, "Pendiente")
    print(f"Reclamación {reclamacion1.id_reclamacion}: {reclamacion1.descripcion}, Estado: {reclamacion1.estado}")

    # Crear pago
    pago1 = Pago(1, poliza1, 5000.00, "Tarjeta de Crédito")
    print(f"Pago {pago1.id_pago}: Monto: {pago1.monto}, Método: {pago1.metodo_pago}")

    # Crear evaluación de riesgo
    evaluacion1 = EvaluacionRiesgo(1, reclamacion1, "Alto", "Accidente grave con múltiples daños")
    print(f"Evaluación {evaluacion1.id_evaluacion}: Nivel de riesgo: {evaluacion1.nivel_riesgo}")
