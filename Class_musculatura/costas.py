import dataclasses

@dataclasses.dataclass
class Costas:
    # Simples (séries)
    costas:             float = 0.0

    # Músculos das costas
    dorsal_superior:    float = 0.0
    dorsal_medial:      float = 0.0
    dorsal_inferior:    float = 0.0

    trapezio_superior:  float = 0.0
    trapezio_medio:     float = 0.0
    trapezio_inferior:  float = 0.0

    redondo_maior:      float = 0.0
    romboide:           float = 0.0

    def set_costas_simples(self, costas):
        self.costas = costas
        return self

    def set_costas_completo(self,
                           dorsal_superior, dorsal_medial, dorsal_inferior,
                           trapezio_superior, trapezio_medio, trapezio_inferior,
                           redondo_maior, romboide):
        self.dorsal_superior        =  dorsal_superior * self.costas
        self.dorsal_medial          = dorsal_medial * self.costas
        self.dorsal_inferior        = dorsal_inferior * self.costas

        self.trapezio_superior      = trapezio_superior * self.costas
        self.trapezio_medio         = trapezio_medio * self.costas
        self.trapezio_inferior      = trapezio_inferior * self.costas

        self.redondo_maior          = redondo_maior * self.costas
        self.romboide               = romboide * self.costas

        return self