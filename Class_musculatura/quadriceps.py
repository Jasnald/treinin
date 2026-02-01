import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Quadriceps(MuscleGroup):
    """
    Representa o volume de treino para o quadríceps, 
    dividido em suas quatro cabeças.
    """
    # Simples (total de séries para o grupo)
    volume: float = 0 

    # Completo (distribuição percentual do volume)
    vasto_lateral:    float = 0
    vasto_medial:     float = 0
    vasto_intermedio: float = 0
    reto_femoral:     float = 0

    def set_volume(self, volume: float):
        """Define o volume total de séries para o quadríceps."""
        self.volume = volume
        return self

    def set_distribution(self, 
                                vasto_lateral: float, vasto_medial: float, 
                                vasto_intermedio: float, reto_femoral: float):
        """Define o volume detalhado para cada porção do quadríceps."""
        self.vasto_lateral    = vasto_lateral    * self.volume
        self.vasto_medial     = vasto_medial     * self.volume
        self.vasto_intermedio = vasto_intermedio * self.volume
        self.reto_femoral     = reto_femoral     * self.volume
        return self
