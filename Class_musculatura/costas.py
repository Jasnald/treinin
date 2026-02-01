import dataclasses
from ._base import MuscleGroup # Import the new base
@dataclasses.dataclass
class Costas(MuscleGroup):
    # Simples (séries)
    volume:             float = 0.0

    # Músculos das costas
    dorsal_superior:    float = 0.0
    dorsal_medial:      float = 0.0
    dorsal_inferior:    float = 0.0

    trapezio_superior:  float = 0.0
    trapezio_medio:     float = 0.0
    trapezio_inferior:  float = 0.0

    redondo_maior:      float = 0.0
    romboide:           float = 0.0

    def set_volume(self, series: float):
        self.volume = series
        return self

    def set_distribution(self,
                           dorsal_superior, dorsal_medial, dorsal_inferior,
                           trapezio_superior, trapezio_medio, trapezio_inferior,
                           redondo_maior, romboide):
        self.dorsal_superior        =  dorsal_superior * self.volume
        self.dorsal_medial          = dorsal_medial * self.volume
        self.dorsal_inferior        = dorsal_inferior * self.volume

        self.trapezio_superior      = trapezio_superior * self.volume
        self.trapezio_medio         = trapezio_medio * self.volume
        self.trapezio_inferior      = trapezio_inferior * self.volume

        self.redondo_maior          = redondo_maior * self.volume
        self.romboide               = romboide * self.volume

        return self