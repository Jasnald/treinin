import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Peito(MuscleGroup):
    # Simples (séries)
    volume:    float = 0.0

    Peito_inferior:     float = 0.0
    Peito_medial:       float = 0.0
    Peito_superior:     float = 0.0
    Serratil:           float = 0.0

    def set_volume(self, volume: float):
        self.volume     = volume
        return self

    def set_distribution(self,
                Peito_inferior, Peito_medial, Peito_superior,
                Serratil):
        self.Peito_inferior     = Peito_inferior    * self.volume
        self.Peito_medial       = Peito_medial      * self.volume
        self.Peito_superior     = Peito_superior    * self.volume
        self.Serratil           = Serratil          * self.volume
        return self

@dataclasses.dataclass
class Ombro(MuscleGroup):
    # Simples (séries)
    volume:    float = 0  

    ombro_anterior:  float = 0
    ombro_medial:    float = 0 
    ombro_posterior: float = 0

    def set_volume(self, volume: float):
        self.volume   = volume
        return self

    def set_distribution(self,
                ombro_anterior, ombro_medial, ombro_posterior):
        self.ombro_anterior     = ombro_anterior    * self.volume
        self.ombro_medial       = ombro_medial      * self.volume
        self.ombro_posterior    = ombro_posterior   * self.volume
        return self
