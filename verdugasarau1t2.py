# ================================================================
# SISTEMA DE CONTROL DE VEHICULOS AUTONOMOS
# ------------------------------------------------
# Proyecto para la Actividad Autónoma - Unidad 1, Tema 2
# Autor: Vladimir (Ciencia de Datos e Inteligencia Artificial - UNACH)
# ================================================================

# Importamos las librerías necesarias
from abc import ABC, abstractmethod

# ================================================================
# SECCION 1: ABSTRACCION Y ENCAPSULAMIENTO
# ================================================================

class Vehiculo(ABC):
    """
    Clase abstracta que representa un vehículo genérico.
    Aplica ABSTRACCION (define lo esencial) y ENCAPSULAMIENTO (atributos protegidos).
    """

    def __init__(self, identificador, modelo, velocidad_maxima, capacidad_carga):
        self._id = identificador              # Atributo protegido
        self._modelo = modelo                 # Atributo protegido
        self._velocidad_maxima = velocidad_maxima
        self._capacidad_carga = capacidad_carga
        self._estrategia_conduccion = None    # Asignaremos una estrategia dinámicamente

    # Getters y Setters (Encapsulamiento)
    def get_modelo(self):
        return self._modelo

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, nueva_velocidad):
        self._velocidad_maxima = nueva_velocidad

    # Métodos abstractos — ABSTRACCIÓN
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

    def informar_estado(self):
        """Muestra información general del vehículo"""
        print(f"[INFO] ID: {self._id}, Modelo: {self._modelo}, "
              f"Velocidad Max: {self._velocidad_maxima} km/h, "
              f"Carga: {self._capacidad_carga} kg")

# ================================================================
# SECCION 2: HERENCIA Y POLIMORFISMO
# ================================================================

class Automovil(Vehiculo):
    """Subclase Automóvil"""
    def acelerar(self):
        print(f"El automóvil {self._modelo} acelera suavemente hasta {self._velocidad_maxima} km/h.")

    def frenar(self):
        print(f"El automóvil {self._modelo} frena con su sistema ABS.")


class Camion(Vehiculo):
    """Subclase Camión"""
    def acelerar(self):
        print(f"El camión {self._modelo} aumenta la velocidad lentamente, alcanzando {self._velocidad_maxima} km/h.")

    def frenar(self):
        print(f"El camión {self._modelo} activa sus frenos neumáticos.")

    def enganchar_remolque(self):
        print(f"El camión {self._modelo} ha enganchado un remolque adicional.")


class Motocicleta(Vehiculo):
    """Subclase Motocicleta"""
    def acelerar(self):
        print(f"La motocicleta {self._modelo} acelera rápidamente hasta {self._velocidad_maxima} km/h.")

    def frenar(self):
        print(f"La motocicleta {self._modelo} frena con maniobras evasivas.")

# ================================================================
# SECCION 3: STRATEGY PATTERN
# ================================================================

class EstrategiaConduccion(ABC):
    """Interfaz para estrategias de conducción"""
    @abstractmethod
    def ejecutar(self):
        pass


class ConduccionEconomica(EstrategiaConduccion):
    def ejecutar(self):
        print("Modo económico: ahorro de combustible y velocidad moderada.")


class ConduccionDeportiva(EstrategiaConduccion):
    def ejecutar(self):
        print("Modo deportivo: máxima aceleración y respuesta rápida.")


class ConduccionOffRoad(EstrategiaConduccion):
    def ejecutar(self):
        print("Modo off-road: tracción en las cuatro ruedas y control de estabilidad.")

# Método para cambiar la estrategia dinámicamente
def asignar_estrategia(vehiculo, estrategia):
    vehiculo._estrategia_conduccion = estrategia
    print(f"Estrategia asignada al {vehiculo.get_modelo()}: {estrategia.__class__.__name__}")
    estrategia.ejecutar()

# ================================================================
# SECCION 4: DECORATOR PATTERN
# ================================================================

class VehiculoDecorator(Vehiculo):
    """Clase base del decorador"""
    def __init__(self, vehiculo):
        self._vehiculo = vehiculo

    def acelerar(self):
        self._vehiculo.acelerar()

    def frenar(self):
        self._vehiculo.frenar()

    def informar_estado(self):
        self._vehiculo.informar_estado()


class PilotoAutomaticoDecorator(VehiculoDecorator):
    def activar_piloto(self):
        print(f"Piloto automático activado en {self._vehiculo.get_modelo()}.")


class AsistenteEstacionamientoDecorator(VehiculoDecorator):
    def activar_asistente(self):
        print(f"Asistente de estacionamiento activado en {self._vehiculo.get_modelo()}.")

# ================================================================
# SECCION 5: SINGLETON PATTERN
# ================================================================

class ControlDeFlota:
    """Clase Singleton para manejar toda la flota de vehículos"""
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ControlDeFlota, cls).__new__(cls)
            cls._instancia._flota = []
        return cls._instancia

    def agregar_vehiculo(self, vehiculo):
        self._flota.append(vehiculo)
        print(f"Vehículo {vehiculo.get_modelo()} agregado a la flota.")

    def mostrar_flota(self):
        print("\n=== Vehículos en la flota ===")
        for v in self._flota:
            v.informar_estado()

    # ================================================================
    # SECCION 6: SOBRECARGA DE OPERADORES
    # ================================================================

    def __add__(self, vehiculo):
        """Permite agregar vehículos con el operador +"""
        self.agregar_vehiculo(vehiculo)
        return self

# ================================================================
# SECCION 7: PRUEBAS DE FUNCIONALIDAD
# ================================================================

if __name__ == "__main__":
    # Creamos vehículos
    auto = Automovil("A1", "Tesla Model 3", 200, 500)
    camion = Camion("C1", "Volvo FH", 120, 20000)
    moto = Motocicleta("M1", "Yamaha R1", 280, 200)

    # Aplicamos estrategias
    asignar_estrategia(auto, ConduccionEconomica())
    asignar_estrategia(moto, ConduccionDeportiva())

    # Decoradores
    auto_con_piloto = PilotoAutomaticoDecorator(auto)
    auto_con_piloto.activar_piloto()

    moto_con_asistente = AsistenteEstacionamientoDecorator(moto)
    moto_con_asistente.activar_asistente()

    # Singleton Control de Flota
    control = ControlDeFlota()
    control + auto
    control + camion
    control + moto

    # Mostrar flota
    control.mostrar_flota()
