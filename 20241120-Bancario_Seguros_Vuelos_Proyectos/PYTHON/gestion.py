class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin=None):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return f"Proyecto: {self.nombre}, Fecha Inicio: {self.fecha_inicio}, Fecha Fin: {self.fecha_fin}"


class Usuario:
    def __init__(self, id_usuario, nombre, email, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"Usuario: {self.nombre}, Email: {self.email}, Rol: {self.rol}"


class Tarea:
    def __init__(self, id_tarea, id_proyecto, id_usuario, descripcion, estado, fecha_asignacion, fecha_entrega=None):
        self.id_tarea = id_tarea
        self.id_proyecto = id_proyecto
        self.id_usuario = id_usuario
        self.descripcion = descripcion
        self.estado = estado
        self.fecha_asignacion = fecha_asignacion
        self.fecha_entrega = fecha_entrega

    def __str__(self):
        return f"Tarea: {self.descripcion}, Estado: {self.estado}, Fecha Asignación: {self.fecha_asignacion}"


class Mensaje:
    def __init__(self, id_mensaje, id_remitente, id_destinatario, contenido, fecha_envio):
        self.id_mensaje = id_mensaje
        self.id_remitente = id_remitente
        self.id_destinatario = id_destinatario
        self.contenido = contenido
        self.fecha_envio = fecha_envio

    def __str__(self):
        return f"Mensaje de Usuario {self.id_remitente} a Usuario {self.id_destinatario}: {self.contenido}"


class Reporte:
    def __init__(self, id_reporte, id_proyecto, titulo, contenido, fecha_generacion):
        self.id_reporte = id_reporte
        self.id_proyecto = id_proyecto
        self.titulo = titulo
        self.contenido = contenido
        self.fecha_generacion = fecha_generacion

    def __str__(self):
        return f"Reporte: {self.titulo}, Fecha: {self.fecha_generacion}"


# Datos iniciales
proyectos = [
    Proyecto(1, 'Proyecto A', 'Descripción del Proyecto A', '2024-01-01', '2024-06-30'),
    Proyecto(2, 'Proyecto B', 'Descripción del Proyecto B', '2024-02-15', '2024-12-31'),
    Proyecto(3, 'Proyecto C', 'Descripción del Proyecto C', '2024-03-01')
]

usuarios = [
    Usuario(1, 'Juan Pérez', 'juan.perez@example.com', 'Administrador'),
    Usuario(2, 'María Gómez', 'maria.gomez@example.com', 'Colaborador'),
    Usuario(3, 'Carlos Rodríguez', 'carlos.rodriguez@example.com', 'Supervisor')
]

tareas = [
    Tarea(1, 1, 1, 'Planificar el proyecto', 'En Progreso', '2024-01-05', '2024-01-15'),
    Tarea(2, 1, 2, 'Desarrollar el módulo A', 'Pendiente', '2024-01-10', '2024-02-28'),
    Tarea(3, 2, 3, 'Revisar los entregables', 'Completado', '2024-02-20', '2024-03-01')
]

mensajes = [
    Mensaje(1, 1, 2, 'Por favor, revisa los requisitos del módulo A.', '2024-01-05'),
    Mensaje(2, 2, 1, 'Revisión en progreso.', '2024-01-06'),
    Mensaje(3, 3, 1, 'El informe ha sido entregado.', '2024-03-02')
]

reportes = [
    Reporte(1, 1, 'Reporte de Avance - Enero', 'El proyecto está en la fase de planificación.', '2024-01-31'),
    Reporte(2, 2, 'Reporte de Avance - Marzo', 'Se completó la revisión de los entregables.', '2024-03-05'),
    Reporte(3, 3, 'Reporte de Estado', 'El proyecto aún no ha iniciado.', '2024-04-01')
]


def main():
    print("=== Proyectos ===")
    for proyecto in proyectos:
        print(proyecto)

    print("\n=== Usuarios ===")
    for usuario in usuarios:
        print(usuario)

    print("\n=== Tareas ===")
    for tarea in tareas:
        print(tarea)

    print("\n=== Mensajes ===")
    for mensaje in mensajes:
        print(mensaje)

    print("\n=== Reportes ===")
    for reporte in reportes:
        print(reporte)


if __name__ == "__main__":
    main()
