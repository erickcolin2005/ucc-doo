# 📝 Análisis de Patrones de Diseño - Proyecto "design-patterns"

Este análisis identifica los patrones de diseño encontrados en el repositorio [`design-patterns`](https://github.com/dannyj182/design-patterns).

---

## 📌 Patrones Creacionales Identificados:

1. **[Abstract Factory](patrones_creacionales/abstract_factory.md)** - Creación de familias de objetos relacionados sin especificar sus clases concretas.
2. **[Builder](patrones_creacionales/builder.md)** - Construcción paso a paso de objetos complejos.
3. **[Factory Method](patrones_creacionales/factory_method.md)** - Creación de objetos mediante una interfaz común sin especificar la clase concreta.
4. **[Prototype](patrones_creacionales/prototype.md)** - Creación de nuevos objetos clonando objetos existentes.
5. **[Singleton](patrones_creacionales/singleton.md)** - Asegura que solo haya una única instancia de una clase en todo el sistema.

Cada patrón está documentado con su respectiva implementación en el código fuente del proyecto.

---

## 📂 Estructura de Archivos

El análisis de cada patrón se encuentra documentado en archivos separados dentro del directorio `patrones_creacionales/`:


Cada archivo incluye:
- 📖 **Explicación del patrón**
- 🖥️ **Código de ejemplo**
- 📌 **Ubicación en el repositorio `design-patterns`**

---

## 🔗 Referencias
- 📂 **Repositorio analizado:** [design-patterns](https://github.com/dannyj182/design-patterns)
- 📖 **Guía de Patrones de Diseño:** [Refactoring.Guru](https://refactoring.guru/design-patterns)

---
🚀 **¡Análisis finalizado!** Ahora puedes explorar cada patrón en detalle en los archivos correspondientes.

# **Análisis de Patrones de Diseño en el Proyecto `design-patterns`**

Este documento presenta un análisis de los patrones de diseño encontrados en el proyecto `design-patterns`. Se han identificado los siguientes patrones creacionales implementados en el código fuente del proyecto:

---

## **1. Abstract Factory**
📍 **Ubicación:** `Patrones Creacionales/Abstract Factory/src/main/java/ar/com/abstract_factory/example/tienda/`

### **📖 Explicación**
El **patrón Abstract Factory** permite la **creación de familias de objetos relacionados sin especificar sus clases concretas**. En este proyecto, se aplica para gestionar la creación de muebles con distintas temáticas.

### **🖥️ Implementación en el proyecto**
- `FabricaMuebles.java` → Interfaz base de la fábrica.
- `FabricaMueblesModernos.java` → Implementación concreta para muebles modernos.
- `FabricaMueblesVictorianos.java` → Implementación concreta para muebles victorianos.
- `Mesa.java`, `Silla.java`, `Sofa.java` → Productos concretos generados por la fábrica.

```java
// Interfaz para las fábricas
public interface FabricaMuebles {
    Mesa crearMesa();
    Silla crearSilla();
}

// Fábrica concreta - Muebles Modernos
public class FabricaMueblesModernos implements FabricaMuebles {
    public Mesa crearMesa() {
        return new MesaModerna();
    }
    public Silla crearSilla() {
        return new SillaModerna();
    }
}
```

---

## **2. Builder**
📍 **Ubicación:** `Patrones Creacionales/Builder/src/main/java/ar/com/builder/example/`

### **📖 Explicación**
El **patrón Builder** permite construir objetos complejos paso a paso. En este proyecto, se utiliza para la creación de diferentes tipos de autos y manuales.

### **🖥️ Implementación en el proyecto**
- `Builder.java` → Interfaz base para la construcción.
- `CarBuilder.java` → Constructor de un auto estándar.
- `CarManualBuilder.java` → Constructor de un manual del auto.

```java
// Interfaz para el Builder
public interface Builder {
    void setEngine(String engine);
    void setWheels(int wheels);
}

// Implementación concreta de un auto
public class CarBuilder implements Builder {
    private String engine;
    private int wheels;

    public void setEngine(String engine) { this.engine = engine; }
    public void setWheels(int wheels) { this.wheels = wheels; }

    public Car build() {
        return new Car(engine, wheels);
    }
}
```

---

## **3. Factory Method**
📍 **Ubicación:** `Patrones Creacionales/Factory Method/src/main/java/ar/com/factory_method/example/logistica/`

### **📖 Explicación**
El **patrón Factory Method** define una interfaz para la creación de objetos, permitiendo que las subclases decidan cuál instanciar.

### **🖥️ Implementación en el proyecto**
- `FabricaTransportes.java` → Interfaz para la fábrica.
- `FabricaBarcos.java`, `FabricaCamiones.java` → Implementaciones concretas.
- `Barco.java`, `Camion.java` → Clases concretas de transporte.

```java
// Interfaz de la fábrica
public abstract class FabricaTransportes {
    public abstract Transporte crearTransporte();
}

// Implementación concreta: Fábrica de camiones
public class FabricaCamiones extends FabricaTransportes {
    public Transporte crearTransporte() {
        return new Camion();
    }
}
```

---

## **4. Prototype**
📍 **Ubicación:** `Patrones Creacionales/Prototype/src/main/java/ar/com/prototype/example/`

### **📖 Explicación**
El **patrón Prototype** permite **clonar objetos en lugar de crearlos desde cero**.

### **🖥️ Implementación en el proyecto**
- `Shape.java` → Clase base con `clone()`.
- `Circle.java`, `Rectangle.java` → Clases concretas.

```java
public class Shape implements Cloneable {
    private String color;

    public Shape(String color) {
        this.color = color;
    }

    public Shape clone() throws CloneNotSupportedException {
        return (Shape) super.clone();
    }
}
```

---

## **5. Singleton**
📍 **Ubicación:** `Patrones Creacionales/Singleton/src/main/java/ar/com/singleton/example/`

### **📖 Explicación**
El **patrón Singleton** asegura que solo exista una única instancia de una clase.

### **🖥️ Implementación en el proyecto**
- `Singleton.java` → Clase con una única instancia.

```java
public class Singleton {
    private static Singleton instancia;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instancia == null) {
            instancia = new Singleton();
        }
        return instancia;
    }
}
```

---

## **📌 Conclusión**

| **Patrón**          | **Uso en el Proyecto** |
|---------------------|------------------------------------------|
| **Abstract Factory** | Creación de familias de muebles (moderno/victoriano). |
| **Builder**         | Construcción paso a paso de autos. |
| **Factory Method**  | Creación de medios de transporte (camion/barco). |
| **Prototype**       | Clonación de objetos de tipo `Shape`. |
| **Singleton**       | Configuración global del sistema. |

Este análisis confirma que el proyecto `design-patterns` implementa diversos patrones de diseño creacionales de manera correcta.

a6fd55c (Añadido análisis de patrones de diseño)
