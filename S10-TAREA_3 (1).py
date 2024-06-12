# Aplicando POO. Realiza una clase que me permita plantear estructuras de datos
# para agregar números en un array y poder visualizarlos ordenados de manera
# ascendente y descendente empleando métodos.

class EstructuraDeDatos:
    def __init__(self):
        self.numeros = []
    
    def agregar_numero(self, numero):
        self.numeros.append(numero)
    
    def ordenar_ascendente(self):
        # Implementación del algoritmo de ordenamiento burbuja (Bubble Sort)
        n = len(self.numeros)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.numeros[j] > self.numeros[j+1]:
                    self.numeros[j], self.numeros[j+1] = self.numeros[j+1], self.numeros[j]
        return self.numeros
    
    def ordenar_descendente(self):
        # Implementación del algoritmo de ordenamiento burbuja (Bubble Sort)
        n = len(self.numeros)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.numeros[j] < self.numeros[j+1]:
                    self.numeros[j], self.numeros[j+1] = self.numeros[j+1], self.numeros[j]
        return self.numeros

    def mostrar_numeros(self):
        return self.numeros

estructura = EstructuraDeDatos()
estructura.agregar_numero(3)
estructura.agregar_numero(1)
estructura.agregar_numero(4)
estructura.agregar_numero(2)

print("Números originales:", estructura.mostrar_numeros())
print("Números ordenados ascendentemente:", estructura.ordenar_ascendente())
print("Números ordenados descendentemente:", estructura.ordenar_descendente())




# Aplicando POO. Realiza una clase que me permita plantear estructuras de datos
# para agregar letras del abecedario en un array y se ordenen alfabéticamente.

class Abecedario:
    def __init__(self):
        self.array = []

    def agregar_letras(self, letras):
        letras_minusculas = letras.lower()
        for letra in letras_minusculas:
            self.array.append(letra)

    def ordenamiento(self):
        # Algoritmo de inserción
        for i in range(1, len(self.array)):  
            clave = self.array[i] 
            j = i - 1  
            while j >= 0 and clave < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = clave  

    def obtener_ordenado(self):
        # Devuelve las letras ordenadas como una cadena
        return ''.join(self.array)

abecedario = Abecedario()
abecedario.agregar_letras("ordenamiento")
abecedario.ordenamiento()
print(abecedario.obtener_ordenado())


#Aplicando POO. Realiza una clase que me permita plantear estructuras de datos
#para realizar una agenda telefónica (nombre, celular) que mediante métodos me
#permita registrar, consultar, eliminar, modificar los datos del contacto y se
#ordenen alfabéticamente empleando diccionarios.

class AgendaTelefonica:
    def __init__(self):
        self.Contactos = {}
    
    def RegistrarContacto(self,nombre,celular):
        if nombre in self.Contactos:
            return'El contacto ya existe'
        
        for numero in self.Contactos.values():
            if numero == celular:
                return 'El número de celular ya existe'
        self.Contactos[nombre] = celular
        return 'Nuevo Contacto Registrado'
        
    def EliminarContacto(self,nombre):
        if nombre in self.Contactos:
            nuevo_contactos = {}
            for item in self.Contactos:
                if item != nombre:
                    nuevo_contactos[item] = self.Contactos[item]
            self.Contactos = nuevo_contactos
            return'Contacto eliminado'
        else:
            return 'Contacto no encontrado'
    
    def ActualizarContacto(self, nombre_antiguo, nombre_nuevo=None, nuevo_celular=None):
        if nombre_antiguo in self.Contactos:
            celular_actual = self.Contactos.pop(nombre_antiguo)
            if nombre_nuevo is None:
                nombre_nuevo = nombre_antiguo
            if nuevo_celular is None:
                nuevo_celular = celular_actual
            self.Contactos[nombre_nuevo] = nuevo_celular
            return f"Contacto '{nombre_antiguo}' modificado con éxito."
        else:
            return 'Contacto no encontrado'
    
    def ConsultarContacto(self,nombre):
        if nombre in self.Contactos:
            return f'Nombre: {nombre} Celular: {self.Contactos[nombre]}'
        else:
            return 'Contacto no encontrado'

    def __str__(self):
        if len(self.Contactos) == 0:
            return 'La agenda está vacía'
        else:
            nombres = list(self.Contactos.keys())
            for i in range(len(nombres)):
                for j in range(0, len(nombres) - i - 1):
                    if nombres[j] > nombres[j + 1]:
                        nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
            result = ''
            for nombre in nombres:
                celular = self.Contactos[nombre]
                result += f'Nombre: {nombre} Celular: {celular}\n'
            return result
agenda = AgendaTelefonica()
agenda.RegistrarContacto('Mateo',99324688)
agenda.RegistrarContacto('Hugo', 983456233)
agenda.RegistrarContacto('Juan', 991224422)
print(agenda.EliminarContacto('Juan'))
print(agenda)



# Revisar, analizar y plantear en líneas de código el algoritmo de Two-Dimensional
# Arrays and Positional Games respecto al juego Tic-Tac-Toe. Libro Data
# Structures and Algorithms in Python, pág. 211

class TicTacToe:
    """Management of a Tic-Tac-Toe game (does not do strategy)."""
    
    def __init__(self):
        """Start a new game."""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
    
    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player's turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self.board[i][j] != '':
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self.board[i][j] = self.player
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    
    def is_win(self, mark):
        """Check whether the board configuration is a win for the given player."""
        board = self.board # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or  # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or  # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or  # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or  # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or  # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or  # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or  # diagonal
                mark == board[0][2] == board[1][1] == board[2][0])    # reverse diagonal
    
    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in 'XO':
            if self.is_win(mark):
                return mark
        return None
    
    def __str__(self):
        """Return string representation of current game board."""
        rows = [' | '.join(self.board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)


