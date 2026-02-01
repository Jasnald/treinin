import dataclasses

# =========================================================
@dataclasses.dataclass
class AbdominalMaquina:
    # Simples (séries)
    abdomen:  float = 10         
    obliquos: float = 2 

    # Completo

    # Reto abdominal
    rectus_superior: float = 0.60
    rectus_inferior: float = 0.40

    # Oblíquos
    obliquo_externo: float = 0.55
    obliquo_interno: float = 0.45

    @property
    def simples(self):
        return (self.abdomen, self.obliquos)

    @property
    def completo(self):
        return (
            # Reto abdominal
            self.abdomen * self.rectus_superior,
            self.abdomen * self.rectus_inferior,

            # Oblíquos
            self.obliquos * self.obliquo_externo,
            self.obliquos * self.obliquo_interno
        )

# =========================================================
@dataclasses.dataclass
class AbdominalInfra:

    # Simples (séries)
    abdomen:          float = 10
    flexores_quadril: float = 4     
    obliquos:         float = 2

    # Completo

    # Reto abdominal (foco maior na parte inferior)
    rectus_inferior: float = 0.70
    rectus_superior: float = 0.30

    # Flexores do quadril
    iliopsoas:      float = 0.50
    reto_femoral:   float = 0.30
    sartorio:       float = 0.20

    # Oblíquos
    obliquo_externo: float = 0.50
    obliquo_interno: float = 0.50

    # -----------------
    @property
    def simples(self):
        return (self.abdomen, self.flexores_quadril, self.obliquos)

    @property
    def completo(self):
        return (
            # Reto abdominal
            self.abdomen * self.rectus_inferior,
            self.abdomen * self.rectus_superior,

            # Flexores do quadril
            self.flexores_quadril * self.iliopsoas,
            self.flexores_quadril * self.reto_femoral,
            self.flexores_quadril * self.sartorio,

            # Oblíquos
            self.obliquos * self.obliquo_externo,
            self.obliquos * self.obliquo_interno
        )
