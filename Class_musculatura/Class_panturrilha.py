import dataclasses

@dataclasses.dataclass
class Panturrilha:
    """
    Representa o volume de treino para as panturrilhas (tríceps sural),
    dividido em seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    panturrilha: float = 0

    # Completo (distribuição percentual do volume)
    gastrocnemio_medial:    float = 0
    gastrocnemio_laterial:  float = 0 
    soleo:                  float = 0

    def set_panturrilha_simples(self, panturrilha: float):
        """Define o volume total de séries para as panturrilhas."""
        self.panturrilha = panturrilha
        return self

    def set_panturrilha_completo(self, 
                                 gastrocnemio_medial: float, 
                                 gastrocnemio_laterial: float, 
                                 soleo: float):
        """Define o volume detalhado para cada porção da panturrilha."""
        self.gastrocnemio_medial    = gastrocnemio_medial   * self.panturrilha
        self.gastrocnemio_laterial  = gastrocnemio_laterial * self.panturrilha
        self.soleo                  = soleo                 * self.panturrilha
        return self

