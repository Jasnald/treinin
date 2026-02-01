import dataclasses

# =========================================================
@dataclasses.dataclass
class ElevacaoLateralMaquina:
    # Simples (séries)
    ombro:    float = 10  
    trapezio: float = 2
    serratus: float = 2   

    # Distribuição Fina

    # Ombro (deltoide) – soma 1.0
    ombro_anterior:  float = 0.15
    ombro_medial:    float = 0.70  
    ombro_posterior: float = 0.15

    # Trapézio – soma 1.0
    trapezio_superior: float = 0.60
    trapezio_medio:    float = 0.30
    trapezio_inferior: float = 0.10

    # Serratus Anterior – soma 1.0
    serratus_superior:   float = 0.30
    serratus_intermedio: float = 0.40
    serratus_inferior:   float = 0.30

    @property
    def simples(self):
        return (self.ombro, self.trapezio, self.serratus)

    @property
    def completo(self):
        return (
            # Ombro
            self.ombro * self.ombro_anterior,
            self.ombro * self.ombro_medial,
            self.ombro * self.ombro_posterior,

            # Trapézio
            self.trapezio * self.trapezio_superior,
            self.trapezio * self.trapezio_medio,
            self.trapezio * self.trapezio_inferior,

            # Serratus Anterior
            self.serratus * self.serratus_superior,
            self.serratus * self.serratus_intermedio,
            self.serratus * self.serratus_inferior
        )
