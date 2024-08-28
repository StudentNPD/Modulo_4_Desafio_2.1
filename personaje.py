class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        
    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp: int):
        tmp_exp = self.experiencia + exp
        print(tmp_exp)
        while tmp_exp >= 100:
            self.nivel += (
                1
            )
            tmp_exp -= 100
        

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= (
                    1
                )
            else:
                tmp_exp = (
                    0
                )

        self.experiencia = tmp_exp

    def __lt__(self, other):
        return (
            self.experiencia < other.experiencia 
        )

    def __gt__(self, other):
        return (
            self.experiencia > other.experiencia
        )

    def __eq__(self, other):
        return (
            self.experiencia == other.experiencia
        )

    def get_probabilidad_ganar(self, other):
        if self.nivel < other.nivel:
            return 0.33
        elif self.nivel > other.nivel:
            return 0.66
        else: 
            return 0.5
    

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganar contra el Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 50. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 30.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
