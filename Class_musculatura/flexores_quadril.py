import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class FlexoresDoQuadril(MuscleGroup):
    """
    Representa o volume de treino para os flexores do quadril.
    Este grupo é ativado principalmente em movimentos de elevação da perna.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    iliopsoas:    float = 0
    sartorio:     float = 0
    reto_femoral: float = 0

    def set_volume(self, series: float):
        """Define o volume total de séries para os flexores do quadril."""
        self.volume = series
        return self

    def set_distribution(self, iliopsoas: float, reto_femoral: float, sartorio: float):
        """Define o volume detalhado para cada músculo do grupo."""
        self.iliopsoas    = iliopsoas    * self.volume
        self.sartorio     = sartorio     * self.volume
        self.reto_femoral = reto_femoral * self.volume
        return self

