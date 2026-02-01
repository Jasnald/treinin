import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class PosteriorCoxa(MuscleGroup):
    """
    Representa o volume de treino para os posteriores da coxa (isquiotibiais),
    dividido por seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    semitendinoso:               float = 0
    semimembranoso:              float = 0
    biceps_femoris_cabeca_longa: float = 0
    biceps_femoris_cabeca_curta: float = 0

    def set_volume(self, volume: float):
        """Define o volume total de séries para os posteriores."""
        self.volume = volume
        return self

    def set_distribution(self, 
                               semitendinoso: float, semimembranoso: float, 
                               biceps_femoris_longa: float, biceps_femoris_curta: float):
        """Define o volume detalhado para cada porção dos posteriores."""
        self.semitendinoso                 = semitendinoso        * self.volume
        self.semimembranoso                = semimembranoso       * self.volume
        self.biceps_femoris_cabeca_longa   = biceps_femoris_longa * self.volume
        self.biceps_femoris_cabeca_curta   = biceps_femoris_curta * self.volume
        return self
