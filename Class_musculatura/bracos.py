import dataclasses

# =========================================================
@dataclasses.dataclass
class Biceps:
    # Simples (séries)
    biceps:    float = 0.0

    biceps_longa: float = 0.0
    biceps_curta: float = 0.0
    braquial:     float = 0.0
   
    def set_biceps_simples(self, biceps):
        self.biceps     = biceps
        return self

    def set_biceps_completo(self,
                biceps_longa, biceps_curta, braquial):
        self.biceps_longa   = biceps_longa  * self.biceps
        self.biceps_curta   = biceps_curta  * self.biceps
        self.braquial       = braquial      * self.biceps
        return self


@dataclasses.dataclass
class Triceps:
    triceps: float = 0.0

    triceps_longa:  float = 0.0
    triceps_medial: float = 0.0
    triceps_curta:  float = 0.0

    def set_triceps_simples(self, triceps):
        self.triceps    = triceps
        return self

    def set_triceps_completo(self,
                triceps_longa, triceps_medial, triceps_curta):
        self.triceps_longa      = triceps_longa     * self.triceps
        self.triceps_medial     = triceps_medial    * self.triceps
        self.triceps_curta      = triceps_curta     * self.triceps
        return self
    
@dataclasses.dataclass
class Antebraco:
    # Simples (séries)
    antebraco: float = 0.0

    braquiorradial:       float = 0.0
    antebraco_fletores:   float = 0.0
    antebraco_extensores: float = 0.0
   
    def set_antebraco_simples(self, antebraco):
        self.antebraco  = antebraco
        return self
    
    def set_antebraco_completo(self,
                braquiorradial, antebraco_fletores, antebraco_extensores):
        self.braquiorradial         = braquiorradial        * self.antebraco
        self.antebraco_fletores     = antebraco_fletores    * self.antebraco
        self.antebraco_extensores   = antebraco_extensores  * self.antebraco
        return self
