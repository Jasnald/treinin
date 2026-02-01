import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Gluteo(MuscleGroup):
    """
    Representa o volume de treino para os glúteos,
    dividido em suas três porções.
    """
    # Simples (total de séries para o grupo)
    volume:         float = 0

    # Completo (distribuição percentual do volume)
    gluteo_maximo:  float = 0
    gluteo_medio:   float = 0
    gluteo_minimo:  float = 0

    def set_volume(self, series: float):
        """Define o volume total de séries para os glúteos."""
        self.volume = series
        return self

    def set_distribution(self, 
                            gluteo_maximo: float, 
                            gluteo_medio: float, 
                            gluteo_minimo: float):
        """Define o volume detalhado para cada porção dos glúteos."""
        self.gluteo_maximo = gluteo_maximo * self.volume
        self.gluteo_medio  = gluteo_medio  * self.volume
        self.gluteo_minimo = gluteo_minimo * self.volume
        return self


