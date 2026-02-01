import dataclasses

@dataclasses.dataclass
class Gluteo:
    """
    Representa o volume de treino para os glúteos,
    dividido em suas três porções.
    """
    # Simples (total de séries para o grupo)
    gluteo:         float = 0

    # Completo (distribuição percentual do volume)
    gluteo_maximo:  float = 0
    gluteo_medio:   float = 0
    gluteo_minimo:  float = 0

    def set_gluteo_simples(self, gluteo: float):
        """Define o volume total de séries para os glúteos."""
        self.gluteo = gluteo
        return self

    def set_gluteo_completo(self, 
                            gluteo_maximo: float, 
                            gluteo_medio: float, 
                            gluteo_minimo: float):
        """Define o volume detalhado para cada porção dos glúteos."""
        self.gluteo_maximo = gluteo_maximo * self.gluteo
        self.gluteo_medio  = gluteo_medio  * self.gluteo
        self.gluteo_minimo = gluteo_minimo * self.gluteo
        return self


