import dataclasses
from ._base import MuscleGroup # Import the new base

# =========================================================
@dataclasses.dataclass
class Biceps(MuscleGroup):
    # Simples (séries)
    volume:    float = 0.0

    biceps_longa: float = 0.0
    biceps_curta: float = 0.0
    braquial:     float = 0.0
   
    def set_volume(self, series: float):
        self.volume     = series
        return self

    def set_distribution(self,
                biceps_longa, biceps_curta, braquial):
        self.biceps_longa   = biceps_longa  * self.volume
        self.biceps_curta   = biceps_curta  * self.volume
        self.braquial       = braquial      * self.volume
        return self


@dataclasses.dataclass
class Triceps(MuscleGroup):
    volume: float = 0.0

    triceps_longa:  float = 0.0
    triceps_medial: float = 0.0
    triceps_curta:  float = 0.0

    def set_volume(self, series: float):
        self.volume    = series
        return self

    def set_distribution(self,
                triceps_longa, triceps_medial, triceps_curta):
        self.triceps_longa      = triceps_longa     * self.volume
        self.triceps_medial     = triceps_medial    * self.volume
        self.triceps_curta      = triceps_curta     * self.volume
        return self
    
@dataclasses.dataclass
class Antebraco(MuscleGroup):
    # Simples (séries)
    volume: float = 0.0

    braquiorradial:       float = 0.0
    antebraco_fletores:   float = 0.0
    antebraco_extensores: float = 0.0
   
    def set_volume(self, series: float):
        self.volume  = series
        return self
    
    def set_distribution(self,
                braquiorradial, antebraco_fletores, antebraco_extensores):
        self.braquiorradial         = braquiorradial        * self.volume
        self.antebraco_fletores     = antebraco_fletores    * self.volume
        self.antebraco_extensores   = antebraco_extensores  * self.volume
        return self
