import dataclasses
from ._base import MuscleGroup # Import the new base

@dataclasses.dataclass
class Manguito(MuscleGroup):
    # Simples (séries)
    volume:       float = 0.0

    # Músculos do manguito rotador
    supraespinhoso: float = 0.0
    infraespinhoso: float = 0.0
    redondo_menor:  float = 0.0
    subescapular:   float = 0.0

    def set_volume(self, volume: float):
        self.volume = volume
        return self

    def set_distribution(self,
                             supraespinhoso, infraespinhoso, 
                             redondo_menor, subescapular):
        self.supraespinhoso = supraespinhoso    * self.volume
        self.infraespinhoso = infraespinhoso    * self.volume
        self.redondo_menor  = redondo_menor     * self.volume
        self.subescapular   = subescapular      * self.volume
        return self