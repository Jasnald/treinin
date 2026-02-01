import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Adutores(MuscleGroup):
    """
    Representa o volume de treino para os adutores da coxa,
    dividido por seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    adutor_magnus: float = 0
    adutor_longus: float = 0
    adutor_brevis: float = 0
    gracilis:      float = 0

    def set_volume(self, series: float):
        """Define o volume total de séries para os adutores."""
        self.volume = series
        return self

    def set_distribution(self, adutor_magnus: float, adutor_longus: float, adutor_brevis: float, gracilis: float):
        """Define o volume detalhado para cada porção dos adutores."""
        self.adutor_magnus = adutor_magnus * self.volume
        self.adutor_longus = adutor_longus * self.volume
        self.adutor_brevis = adutor_brevis * self.volume
        self.gracilis      = gracilis      * self.volume
        return self

