import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Abdomen(MuscleGroup):
    """
    Representa o volume de treino para a musculatura do abdômen,
    dividido entre o reto abdominal e os oblíquos.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    # Reto Abdominal
    reto_abdominal_superior: float = 0
    reto_abdominal_inferior: float = 0

    # Oblíquos
    obliquo_externo: float = 0
    obliquo_interno: float = 0

    def set_volume(self, series: float):
        """Define o volume total de séries para o abdômen."""
        self.volume = series
        return self

    def set_distribution(self, 
                             reto_superior: float, reto_inferior: float, 
                             obliquo_externo: float, obliquo_interno: float):
        """Define o volume detalhado para cada porção do abdômen."""

        # Distribui o volume dentro de cada subgrupo
        self.reto_abdominal_superior = reto_superior    * self.volume
        self.reto_abdominal_inferior = reto_inferior    * self.volume
        self.obliquo_externo         = obliquo_externo  * self.volume
        self.obliquo_interno         = obliquo_interno  * self.volume
        return self

@dataclasses.dataclass
class Lombar(MuscleGroup):
    """
    Representa o volume de treino para os músculos extensores da coluna,
    incluindo os paravertebrais e outros estabilizadores.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0

    # Completo (distribuição percentual do volume)
    eretores_da_espinha: float = 0
    multifidus:          float = 0
    quadrado_lombar:     float = 0

    def set_volume(self, series: float):
        """Define o volume total de séries para a região lombar."""
        self.volume = series
        return self

    def set_distribution(self, 
                            eretores        : float, 
                            multifidus      : float, 
                            quadrado_lombar : float):
        """Define o volume detalhado para cada músculo da região lombar."""
        self.eretores_da_espinha = eretores        * self.volume
        self.multifidus          = multifidus      * self.volume
        self.quadrado_lombar     = quadrado_lombar * self.volume
        return self