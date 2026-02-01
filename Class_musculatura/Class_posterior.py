import dataclasses

@dataclasses.dataclass
class PosteriorCoxa:
    """
    Representa o volume de treino para os posteriores da coxa (isquiotibiais),
    dividido por seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    posteriorcoxa: float = 0

    # Completo (distribuição percentual do volume)
    semitendinoso:               float = 0
    semimembranoso:              float = 0
    biceps_femoris_cabeca_longa: float = 0
    biceps_femoris_cabeca_curta: float = 0

    def set_posteriorcoxa_simples(self, posteriorcoxa: float):
        """Define o volume total de séries para os posteriores."""
        self.posteriorcoxa = posteriorcoxa
        return self

    def set_posteriorcoxa_completo(self, 
                               semitendinoso: float, semimembranoso: float, 
                               biceps_femoris_longa: float, biceps_femoris_curta: float):
        """Define o volume detalhado para cada porção dos posteriores."""
        self.semitendinoso                 = semitendinoso        * self.posteriorcoxa
        self.semimembranoso                = semimembranoso       * self.posteriorcoxa
        self.biceps_femoris_cabeca_longa   = biceps_femoris_longa * self.posteriorcoxa
        self.biceps_femoris_cabeca_curta   = biceps_femoris_curta * self.posteriorcoxa
        return self
