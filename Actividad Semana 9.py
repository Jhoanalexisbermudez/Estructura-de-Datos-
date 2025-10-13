import time
import random
import threading

class Nodo:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.anterior = None
        self.siguiente = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_jugador(self, nombre, puntaje):
        nuevo = Nodo(nombre, puntaje)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            actual = self.cabeza
            while actual and actual.puntaje >= puntaje:
                actual = actual.siguiente
            if actual == self.cabeza:
                nuevo.siguiente = self.cabeza
                self.cabeza.anterior = nuevo
                self.cabeza = nuevo
            elif actual is None:
                self.cola.siguiente = nuevo
                nuevo.anterior = self.cola
                self.cola = nuevo
            else:
                nuevo.siguiente = actual
                nuevo.anterior = actual.anterior
                actual.anterior.siguiente = nuevo
                actual.anterior = nuevo
        self.limitar_top5()

    def limitar_top5(self):
        actual = self.cabeza
        contador = 1
        while actual and contador < 5:
            actual = actual.siguiente
            contador += 1
        if actual and actual.siguiente:
            actual.siguiente = None
            self.cola = actual

    def mostrar_ranking(self):
        print("\n--- RANKING TOP 5 ---")
        actual = self.cabeza
        pos = 1
        while actual:
            print(f"{pos}. {actual.nombre} - {actual.puntaje} pts")
            actual = actual.siguiente
            pos += 1



ranking = ListaDoblementeEnlazada()

def jugar(nombre):
    nivel = 1
    tiempo = 10
    puntaje = 0

    while True:
        print(f"\n--- Nivel {nivel} ---")
        for i in range(1, 6):
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            resultado = a + b
            print(f"Suma {i}: {a} + {b} = ?")

            respuesta = leer_con_tiempo(tiempo)
            if respuesta is None:
                print("⏰ Tiempo agotado!")
                return puntaje

            try:
                respuesta = int(respuesta)
            except ValueError:
                print("❌ Entrada inválida.")
                return puntaje

            if respuesta == resultado:
                puntaje += 100
                print("✅ Correcto! +100 puntos")
            else:
                print("❌ Incorrecto.")
                return puntaje

        nivel += 1
        tiempo = max(2, tiempo - 2)
        print(f"⏩ Nivel completado. Tiempo por operación ahora: {tiempo} seg")


def leer_con_tiempo(segundos):
    """Lee la entrada del usuario con límite de tiempo."""
    respuesta = [None]

    def leer():
        try:
            respuesta[0] = input("> ")
        except:
            pass

    hilo = threading.Thread(target=leer)
    hilo.start()
    hilo.join(timeout=segundos)
    if hilo.is_alive():
        return None
    return respuesta[0]



def main():
    while True:
        nombre = input("Ingrese su nombre de jugador: ")
        puntaje = jugar(nombre)
        print(f"\nPuntaje final: {puntaje}")
        ranking.agregar_jugador(nombre, puntaje)
        ranking.mostrar_ranking()

        opc = input("\n¿Desea jugar de nuevo? (s/n): ").lower()
        if opc != "s":
            break


if __name__ == "__main__":
    main()
