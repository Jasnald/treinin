import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Panturrilha(MuscleGroup):
    """
    Representa o volume de treino para as panturrilhas (tríceps sural),
    dividido em seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    gastrocnemio_medial:    float = 0
    gastrocnemio_laterial:  float = 0 
    soleo:                  float = 0

    def set_volume(self, volume: float):
        """Define o volume total de séries para as panturrilhas."""
        self.volume = volume
        return self

    def set_distribution(self, 
                                 gastrocnemio_medial: float, 
                                 gastrocnemio_laterial: float, 
                                 soleo: float):
        """Define o volume detalhado para cada porção da panturrilha."""
        self.gastrocnemio_medial    = gastrocnemio_medial   * self.volume
        self.gastrocnemio_laterial  = gastrocnemio_laterial * self.volume
        self.soleo                  = soleo                 * self.volume
        return self

