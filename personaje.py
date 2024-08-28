class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        

    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    @estado.setter
    def estado(self, exp):
        temp_exp = self.experiencia + exp
        if self.nivel==1 and exp<0 and (temp_exp)<0:
            
            self.nivel=1 
            self.experiencia=0 
        elif self.nivel>1 and exp<0 and (temp_exp)<0:
            
            self.nivel-=1 
            self.experiencia=100+ temp_exp  
        elif self.nivel>1 and exp<0 and (temp_exp)==0:
            self.experiencia=100+ temp_exp  
      
        elif self.nivel>=1 and exp>=0 and (temp_exp)<100:
            #self.nivel=1 
            self.experiencia=self.experiencia + exp
        elif self.nivel>=1 and exp>=0 and (temp_exp)>=100:
           
            self.nivel+=1
            #print(temp_exp)
            #print((temp_exp - 100 ) )
            self.experiencia=(temp_exp - 100 ) 
            
        elif self.nivel==1 and exp<0 and (temp_exp)>0:
            #self.nivel=1 
            self.experiencia=temp_exp

        
       # tmp_exp = self.experiencia + exp

        #while tmp_exp >= 100:
        #    self.nivel += (
        #        2
        #    )
        #    tmp_exp -= 90

        #while tmp_exp < 0:
        #    if self.nivel > 1:
        #        tmp_exp = 100 + tmp_exp
        #        self.nivel -= (
        #            2
        #        )
        #    else:
        #        tmp_exp = (
        #            -1
        #        )

        #self.experiencia = tmp_exp

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
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else: 
            return 0.5

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de perder contra el Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
