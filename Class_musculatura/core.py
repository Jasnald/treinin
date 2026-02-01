import dataclasses

@dataclasses.dataclass
class Abdomen:
    """
    Representa o volume de treino para a musculatura do abdômen,
    dividido entre o reto abdominal e os oblíquos.
    """
    # Simples (total de séries para o grupo)
    abdomen: float = 0

    # Completo (distribuição percentual do volume)
    # Reto Abdominal
    reto_abdominal_superior: float = 0
    reto_abdominal_inferior: float = 0

    # Oblíquos
    obliquo_externo: float = 0
    obliquo_interno: float = 0

    def set_abdomen_simples(self, abdomen: float):
        """Define o volume total de séries para o abdômen."""
        self.abdomen = abdomen
        return self

    def set_abdomen_completo(self, 
                             reto_superior: float, reto_inferior: float, 
                             obliquo_externo: float, obliquo_interno: float):
        """Define o volume detalhado para cada porção do abdômen."""

        # Distribui o volume dentro de cada subgrupo
        self.reto_abdominal_superior = reto_superior    * self.abdomen
        self.reto_abdominal_inferior = reto_inferior    * self.abdomen
        self.obliquo_externo         = obliquo_externo  * self.abdomen
        self.obliquo_interno         = obliquo_interno  * self.abdomen
        return self

@dataclasses.dataclass
class Lombar:
    """
    Representa o volume de treino para os músculos extensores da coluna,
    incluindo os paravertebrais e outros estabilizadores.
    """
    # Simples (total de séries para o grupo)
    lombar: float = 0

    # Completo (distribuição percentual do volume)
    eretores_da_espinha: float = 0
    multifidus:          float = 0
    quadrado_lombar:     float = 0

    def set_lombar_simples(self, lombar: float):
        """Define o volume total de séries para a região lombar."""
        self.lombar = lombar
        return self

    def set_lombar_completo(self, 
                            eretores        : float, 
                            multifidus      : float, 
                            quadrado_lombar : float):
        """Define o volume detalhado para cada músculo da região lombar."""
        self.eretores_da_espinha = eretores        * self.lombar
        self.multifidus          = multifidus      * self.lombar
        self.quadrado_lombar     = quadrado_lombar * self.lombar
        return self