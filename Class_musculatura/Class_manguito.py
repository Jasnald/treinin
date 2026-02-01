import dataclasses

@dataclasses.dataclass
class Manguito:
    # Simples (séries)
    manguito:       float = 0.0

    # Músculos do manguito rotador
    supraespinhoso: float = 0.0
    infraespinhoso: float = 0.0
    redondo_menor:  float = 0.0
    subescapular:   float = 0.0

    def set_manguito_simples(self, manguito):
        self.manguito = manguito
        return self

    def set_manguito_completo(self,
                             supraespinhoso, infraespinhoso, 
                             redondo_menor, subescapular):
        self.supraespinhoso = supraespinhoso    * self.manguito
        self.infraespinhoso = infraespinhoso    * self.manguito
        self.redondo_menor  = redondo_menor     * self.manguito
        self.subescapular   = subescapular      * self.manguito
        return self