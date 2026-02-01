import dataclasses

# =========================================================
@dataclasses.dataclass
class RDL:
    # Simples (séries)
    posteriores_coxa: float = 8   
    gluteos:          float = 10
    lombar:           float = 5
    adutores:         float = 1

    # Completo
    # Isquiotibiais (soma 1.0)
    semitendinoso:                 float = 0.30
    semimembranoso:                float = 0.25
    biceps_femoris_cabeca_longa:   float = 0.30
    biceps_femoris_cabeca_curta:   float = 0.15

    # Glúteos (soma 1.0)
    gluteo_maximo: float = 0.70
    gluteo_medio:  float = 0.20
    gluteo_minimo: float = 0.10

    # Lombar (soma 1.0)
    erector_spinae: float = 0.80
    multifidus:     float = 0.20

    # Adutores (soma 1.0)
    adutor_magnus: float = 0.75
    adutor_longus: float = 0.25

    # -----------------
    @property
    def simples(self):
        return (
            self.posteriores_coxa,
            self.gluteos,
            self.lombar,
            self.adutores
        )

    @property
    def completo(self):
        return (
            # Posteriores de coxa
            self.posteriores_coxa * self.semitendinoso,
            self.posteriores_coxa * self.semimembranoso,
            self.posteriores_coxa * self.biceps_femoris_cabeca_longa,
            self.posteriores_coxa * self.biceps_femoris_cabeca_curta,

            # Glúteos
            self.gluteos * self.gluteo_maximo,
            self.gluteos * self.gluteo_medio,
            self.gluteos * self.gluteo_minimo,

            # Lombar
            self.lombar * self.erector_spinae,
            self.lombar * self.multifidus,

            # Adutores
            self.adutores * self.adutor_magnus,
            self.adutores * self.adutor_longus
        )

# =========================================================
@dataclasses.dataclass
class CadeiraFlexora:
    # Simples
    posteriores_coxa: float = 10
    gluteos:          float = 1      
    panturrilha:      float = 3    

    # Isquiotibiais
    semitendinoso:               float = 0.35
    semimembranoso:              float = 0.30
    biceps_femoris_cabeca_longa: float = 0.25
    biceps_femoris_cabeca_curta: float = 0.10

    # Glúteos
    gluteo_maximo: float = 0.80
    gluteo_medio:  float = 0.15
    gluteo_minimo: float = 0.05

    # Panturrilha
    gastrocnemio: float = 0.70
    soleo:        float = 0.30

    @property
    def simples(self):
        return (self.posteriores_coxa, self.gluteos, self.panturrilha)

    @property
    def completo(self):
        return (
            # Posteriores de coxa
            self.posteriores_coxa * self.semitendinoso,
            self.posteriores_coxa * self.semimembranoso,
            self.posteriores_coxa * self.biceps_femoris_cabeca_longa,
            self.posteriores_coxa * self.biceps_femoris_cabeca_curta,

            # Glúteos
            self.gluteos * self.gluteo_maximo,
            self.gluteos * self.gluteo_medio,
            self.gluteos * self.gluteo_minimo,

            # Panturrilha
            self.panturrilha * self.gastrocnemio,
            self.panturrilha * self.soleo
        )

# =========================================================
@dataclasses.dataclass
class BackExtension:
    # Simples
    lombar:           float = 8
    gluteos:          float = 10
    posteriores_coxa: float = 6

    # Lombar
    erector_spinae: float = 0.80
    multifidus:     float = 0.20

    # Glúteos
    gluteo_maximo: float = 0.75
    gluteo_medio:  float = 0.18
    gluteo_minimo: float = 0.07

    # Posteriores de coxa
    semitendinoso:               float = 0.30
    semimembranoso:              float = 0.30
    biceps_femoris_cabeca_longa: float = 0.25
    biceps_femoris_cabeca_curta: float = 0.15

    @property
    def simples(self):
        return (self.lombar, self.gluteos, self.posteriores_coxa)

    @property
    def completo(self):
        return (
            # Lombar
            self.lombar * self.erector_spinae,
            self.lombar * self.multifidus,

            # Glúteos
            self.gluteos * self.gluteo_maximo,
            self.gluteos * self.gluteo_medio,
            self.gluteos * self.gluteo_minimo,

            # Posteriores de coxa
            self.posteriores_coxa * self.semitendinoso,
            self.posteriores_coxa * self.semimembranoso,
            self.posteriores_coxa * self.biceps_femoris_cabeca_longa,
            self.posteriores_coxa * self.biceps_femoris_cabeca_curta
        )

# =========================================================
@dataclasses.dataclass
class LegPress:
    # Simples (séries)
    quadriceps:      float = 10
    gluteos:         float = 5
    adutores:        float = 3
    posteriores_coxa: float = 1

    # Completo

    # Quadríceps (soma 1.0)
    vasto_lateral:      float = 0.4
    vasto_medial:       float = 0.3
    vasto_intermedio:   float = 0.3
    reto_femoral:       float = 0.0

    # Glúteos
    gluteo_maximo: float = 0.60
    gluteo_medio:  float = 0.30
    gluteo_minimo: float = 0.10

    # Adutores
    adutor_magnus: float = 0.40
    adutor_longus: float = 0.35
    adutor_brevis: float = 0.15
    gracilis:      float = 0.10

    # Posteriores de coxa
    semitendinoso:               float = 0.03
    semimembranoso:              float = 0.03
    biceps_femoris_cabeca_longa: float = 0.03
    biceps_femoris_cabeca_curta: float = 0.91

    # -----------------
    @property
    def simples(self):
        return (
            self.quadriceps,
            self.gluteos,
            self.adutores,
            self.posteriores_coxa
        )

    @property
    def completo(self):
        return (
            # Quadríceps
            self.quadriceps * self.vasto_lateral,
            self.quadriceps * self.vasto_medial,
            self.quadriceps * self.vasto_intermedio,
            self.quadriceps * self.reto_femoral,

            # Glúteos
            self.gluteos * self.gluteo_maximo,
            self.gluteos * self.gluteo_medio,
            self.gluteos * self.gluteo_minimo,

            # Adutores
            self.adutores * self.adutor_magnus,
            self.adutores * self.adutor_longus,
            self.adutores * self.adutor_brevis,
            self.adutores * self.gracilis,

            # Posteriores de coxa
            self.posteriores_coxa * self.semitendinoso,
            self.posteriores_coxa * self.semimembranoso,
            self.posteriores_coxa * self.biceps_femoris_cabeca_longa,
            self.posteriores_coxa * self.biceps_femoris_cabeca_curta
        )

# =========================================================
@dataclasses.dataclass
class SissySquat:
    quadriceps:      float = 10
    gluteos:         float = 1
    adutores:        float = 1

    # Quadríceps
    reto_femoral:     float = 0.4
    vasto_medial:     float = 0.2
    vasto_lateral:    float = 0.2
    vasto_intermedio: float = 0.2

    # Glúteos
    gluteo_maximo: float = 0.70
    gluteo_medio:  float = 0.20
    gluteo_minimo: float = 0.10

    # Adutores
    adutor_magnus: float = 0.45
    adutor_longus: float = 0.35
    adutor_brevis: float = 0.20

    @property
    def simples(self):
        return (self.quadriceps, self.gluteos, self.adutores)

    @property
    def completo(self):
        return (
            # Quadríceps
            self.quadriceps * self.reto_femoral,
            self.quadriceps * self.vasto_medial,
            self.quadriceps * self.vasto_lateral,
            self.quadriceps * self.vasto_intermedio,

            # Glúteos
            self.gluteos * self.gluteo_maximo,
            self.gluteos * self.gluteo_medio,
            self.gluteos * self.gluteo_minimo,

            # Adutores
            self.adutores * self.adutor_magnus,
            self.adutores * self.adutor_longus,
            self.adutores * self.adutor_brevis
        )

# =========================================================
@dataclasses.dataclass
class LegExtension:
    quadriceps: float = 10

    # Quadríceps
    reto_femoral:     float = 0.4
    vasto_medial:     float = 0.2
    vasto_lateral:    float = 0.2
    vasto_intermedio: float = 0.2

    @property
    def simples(self):
        return (self.quadriceps)

    @property
    def completo(self):
        return (
            self.quadriceps * self.vasto_medial,
            self.quadriceps * self.vasto_lateral,
            self.quadriceps * self.reto_femoral,
            self.quadriceps * self.vasto_intermedio
        )

# =========================================================
@dataclasses.dataclass
class PanturrilhaLegPress:
    # Simples (séries)
    panturrilha: float = 10
    tibial:      float = 2      

    # Completo
    # Tríceps sural (soma 1.0)
    gastrocnemio_medial:  float = 0.45
    gastrocnemio_lateral: float = 0.35
    soleo:                float = 0.20

    # Tibial / dorsiflexores (soma 1.0)
    tibialis_anterior:     float = 0.60
    extensor_digital_longo: float = 0.40

    # -----------------
    @property
    def simples(self):
        return (self.panturrilha, self.tibial)

    @property
    def completo(self):
        return (
            # Panturrilha (tríceps sural)
            self.panturrilha * self.gastrocnemio_medial,
            self.panturrilha * self.gastrocnemio_lateral,
            self.panturrilha * self.soleo,
            # Tibial / dorsiflexores
            self.tibial * self.tibialis_anterior,
            self.tibial * self.extensor_digital_longo
        )
