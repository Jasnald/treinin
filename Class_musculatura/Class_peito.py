import dataclasses

# =========================================================
@dataclasses.dataclass
class Peito:
    # Simples (séries)
    Peito:    float = 0.0

    Peito_inferior:     float = 0.0
    Peito_medial:       float = 0.0
    Peito_superior:     float = 0.0
    Serratil:           float = 0.0

    def set_peito_simples(self, Peito):
        self.Peito     = Peito
        return self

    def set_peito_completo(self,
                Peito_inferior, Peito_medial, Peito_superior,
                Serratil):
        self.Peito_inferior     = Peito_inferior    * self.Peito
        self.Peito_medial       = Peito_medial      * self.Peito
        self.Peito_superior     = Peito_superior    * self.Peito
        self.Serratil           = Serratil          * self.Peito
        return self

@dataclasses.dataclass
class Ombro:
    # Simples (séries)
    ombro:    float = 0  

    ombro_anterior:  float = 0
    ombro_medial:    float = 0 
    ombro_posterior: float = 0

    def set_ombro_simples(self, ombro):
        self.ombro     = ombro
        return self

    def set_ombro_completo(self,
                ombro_anterior, ombro_medial, ombro_posterior):
        self.ombro_anterior     = ombro_anterior    * self.ombro
        self.ombro_medial       = ombro_medial      * self.ombro
        self.ombro_posterior    = ombro_posterior   * self.ombro
        return self
