import dataclasses

@dataclasses.dataclass
class Adutores:
    """
    Representa o volume de treino para os adutores da coxa,
    dividido por seus principais músculos.
    """
    # Simples (total de séries para o grupo)
    adutores: float = 0

    # Completo (distribuição percentual do volume)
    adutor_magnus: float = 0
    adutor_longus: float = 0
    adutor_brevis: float = 0
    gracilis:      float = 0

    def set_adutores_simples(self, adutores: float):
        """Define o volume total de séries para os adutores."""
        self.adutores = adutores
        return self

    def set_adutores_completo(self, adutor_magnus: float, adutor_longus: float, adutor_brevis: float, gracilis: float):
        """Define o volume detalhado para cada porção dos adutores."""
        self.adutor_magnus = adutor_magnus * self.adutores
        self.adutor_longus = adutor_longus * self.adutores
        self.adutor_brevis = adutor_brevis * self.adutores
        self.gracilis      = gracilis      * self.adutores
        return self

