#Creación de la clase 'Personaje'
class Personaje:
    '''Constructor de la clase, que recibe el nombre del personaje'''
    def __init__(self,nombre: str):
        self.nombre = nombre
        self.nivel  = 1
        self.exp    = 0
        
    @property    
    def estado (self):
        return f"\n Nombre personaje : {self.nombre}\n Nivel : {self.nivel}\n Experiencia : {self.exp}\n "
    @estado.setter
    def estado(self, exp_recibida: int):
        exp_valor = self.exp + exp_recibida
    
    # Verificar si la experiencia acumulada supera o iguala los 100 puntos
        if exp_valor >= 100:
        # Calcular cuántos niveles sube el personaje y cuánta experiencia queda
            niveles_subidos = exp_valor // 100
            exp_restante = exp_valor % 100
        
        # Ajustar el nivel y la experiencia acumulada
            self.nivel += niveles_subidos
            self.exp = exp_restante
        
    # Verificar si la experiencia acumulada es negativa
        elif exp_valor < 0:
        # Calcular la nueva experiencia acumulada después de restar la experiencia recibida
            exp_restante = self.exp + exp_recibida
        
        # Verificar si el personaje baja de nivel
            if exp_restante < 0:
            # Si el nivel es mayor que 1, reducir el nivel en 1 y ajustar la experiencia acumulada
                if self.nivel > 1:
                    self.nivel -= 1
                    self.exp = 100 + exp_restante  # Agregar 100 puntos a la experiencia restante
                else:
                    self.exp = 0  # Si el nivel es 1, establecer la experiencia acumulada a 0
            else:
                self.exp = exp_restante  # Si no, establecer la nueva experiencia acumulada
    
        else:
            self.exp = exp_valor  # Si no se cumple ninguna de las condiciones anteriores, 
            # establecer la experiencia acumulada directamente
    
    # Verificar si el nivel es menor que 1 y ajustarlo a 1
        if self.nivel < 1:
            self.nivel = 1
        
    
    def __gt__(self,other):
        # Metodo especial para comparar si un personaje es mayor que otro (sobrecarga del operador ">")

        return self.nivel > other.nivel
    
    def __lt__(self,other):
        
        # Metodo especial para comparar si un personaje es menor que otro (sobrecarga del operador "<")
        return self.nivel < other.nivel
    
    
    # Metodo que calcula la probabilidad de que el personaje actual gane en una batalla contra otro personaje

    def probabilidad(self, other):
        if self.nivel > other.nivel:
            return 0.66
        elif self.nivel < other.nivel:
            return 0.33
        elif self.nivel == other.nivel:
            return 0.5
    
    # Metodo estático que muestra un diálogo de enfrentamiento al orco
    @staticmethod
    def dialogo_batalla(probabilidad):
        print(f"Tienes una probabilidad de {probabilidad*100} % de ganar, suerte!")
        print("En caso de ganar, recibirás 50 puntos de experiencia y el orco perdera 30 puntos")
        print("En caso de perder, perderás 30 puntos de experiencia y el orco ganar 50 puntos")