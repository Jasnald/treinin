import dataclasses

# =========================================================
@dataclasses.dataclass
class CableCurl:
    # Simples (séries)
    biceps:    float = 10
    antebraco: float = 4

    # Completo

    # Bíceps (soma 1.0)
    biceps_longa: float = 0.4
    biceps_curta: float = 0.4
    braquial:     float = 0.2

    # Antebraço (soma 1.0)
    braquiorradial:       float = 0.6
    antebraco_fletores:   float = 0.2
    antebraco_extensores: float = 0.2

    @property
    def simples(self):
        return (self.biceps, self.antebraco)

    @property
    def completo(self):
        return (
            # Bíceps
            self.biceps * self.biceps_longa,
            self.biceps * self.biceps_curta,
            # Antebraço
            self.antebraco * self.braquiorradial,
            self.antebraco * self.antebraco_fletores,
            self.antebraco * self.antebraco_extensores
        )

# =========================================================
@dataclasses.dataclass
class RoscaMartelo:
    biceps:    float = 10
    antebraco: float = 8

    # Bíceps (incluindo braquial) – soma 1.0
    biceps_longa: float = 0.45
    biceps_curta: float = 0.25
    braquial:     float = 0.30

    # Antebraço
    braquiorradial:       float = 0.80
    antebraco_fletores:   float = 0.10
    antebraco_extensores: float = 0.10

    @property
    def simples(self):
        return (self.biceps, self.antebraco)

    @property
    def completo(self):
        return (
            # Bíceps / Braquial
            self.biceps * self.biceps_longa,
            self.biceps * self.biceps_curta,
            self.biceps * self.braquial,
            # Antebraço
            self.antebraco * self.braquiorradial,
            self.antebraco * self.antebraco_fletores,
            self.antebraco * self.antebraco_extensores
        )

# =========================================================
@dataclasses.dataclass
class TricepsPulldown:
    triceps: float = 10
    ombro:   float = 1 


    # Tríceps (soma 1.0)
    triceps_longa: float = 0.40
    triceps_media: float = 0.35
    triceps_curta: float = 0.25

    # Ombro (deltoide anterior / medial ‒ soma 1.0)
    ombro_anterior:   float = 0.4
    ombro_medial:     float = 0.3
    ombro_posterior:  float = 0.2


    @property
    def simples(self):
        return (self.triceps, self.ombro)

    @property
    def completo(self):
        return (
            # Tríceps
            self.triceps * self.triceps_longa,
            self.triceps * self.triceps_media,
            self.triceps * self.triceps_curta,
            # Ombro
            self.ombro * self.ombro_anterior,
            self.ombro * self.ombro_medial,
            self.ombro * self.ombro_posterior
        )
