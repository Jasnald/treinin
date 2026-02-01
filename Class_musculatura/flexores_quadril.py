import dataclasses

@dataclasses.dataclass
class FlexoresDoQuadril:
    """
    Representa o volume de treino para os flexores do quadril.
    Este grupo é ativado principalmente em movimentos de elevação da perna.
    """
    # Simples (total de séries para o grupo)
    flexores_quadril: float = 0

    # Completo (distribuição percentual do volume)
    iliopsoas:    float = 0
    sartorio:     float = 0

    def set_flexores_simples(self, flexores_quadril: float):
        """Define o volume total de séries para os flexores do quadril."""
        self.flexores_quadril = flexores_quadril
        return self

    def set_flexores_completo(self, iliopsoas: float, reto_femoral: float, sartorio: float):
        """Define o volume detalhado para cada músculo do grupo."""
        self.iliopsoas    = iliopsoas    * self.flexores_quadril
        self.sartorio     = sartorio     * self.flexores_quadril
        return self

