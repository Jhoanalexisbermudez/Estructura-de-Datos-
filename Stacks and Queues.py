class Pila:
    def __init__(self, max):
        self.max = max
        self.elementos = [0] * max
        self.tope = -1

    def push(self, valor):
        if self.tope < self.max - 1:
            self.tope += 1
            self.elementos[self.tope] = valor
        else:
            print("La pila está llena")

    def pop(self):
        if self.tope >= 0:
            valor = self.elementos[self.tope]
            self.tope -= 1
            return valor
        else:
            print("La pila está vacía")
            return -1

    def pintar_pila(self):
        print("Contenido de la pila:")
        for i in range(self.tope, -1, -1):
            print(f"| {self.elementos[i]} |")
        print("-----")


class Cola:
    def __init__(self, max):
        self.max = max
        self.elementos = [0] * max
        self.frente = 0
        self.fin = -1
        self.tamaño = 0

    def encolar(self, valor):
        if self.tamaño < self.max:
            self.fin = (self.fin + 1) % self.max
            self.elementos[self.fin] = valor
            self.tamaño += 1
        else:
            print("La cola está llena")

    def desencolar(self):
        if self.tamaño > 0:
            valor = self.elementos[self.frente]
            self.frente = (self.frente + 1) % self.max
            self.tamaño -= 1
            return valor
        else:
            print("La cola está vacía")
            return -1

    def pintar_cola(self):
        print("Contenido de la cola:")
        for i in range(self.tamaño):
            index = (self.frente + i) % self.max
            print(self.elementos[index], end=" ")
        print()


class Principal:
    @staticmethod
    def main():
        pila = Pila(5)
        for i in range(1, 6):
            pila.push(i)
        pila.pintar_pila()
        pila.pop()
        print("Después de hacer pop:")
        pila.pintar_pila()

        print("---------------------------")

        cola = Cola(5)
        for i in range(1, 6):
            cola.encolar(i)
        cola.pintar_cola()
        cola.desencolar()
        print("Después de hacer desencolar:")
        cola.pintar_cola()


if __name__ == "__main__":
    Principal.main()
