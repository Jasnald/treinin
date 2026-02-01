import dataclasses

@dataclasses.dataclass
class Quadriceps:
    """
    Representa o volume de treino para o quadríceps, 
    dividido em suas quatro cabeças.
    """
    # Simples (total de séries para o grupo)
    quadriceps: float = 0 

    # Completo (distribuição percentual do volume)
    vasto_lateral:    float = 0
    vasto_medial:     float = 0
    vasto_intermedio: float = 0
    reto_femoral:     float = 0

    def set_quadriceps_simples(self, quadriceps: float):
        """Define o volume total de séries para o quadríceps."""
        self.quadriceps = quadriceps
        return self

    def set_quadriceps_completo(self, 
                                vasto_lateral: float, vasto_medial: float, 
                                vasto_intermedio: float, reto_femoral: float):
        """Define o volume detalhado para cada porção do quadríceps."""
        self.vasto_lateral    = vasto_lateral    * self.quadriceps
        self.vasto_medial     = vasto_medial     * self.quadriceps
        self.vasto_intermedio = vasto_intermedio * self.quadriceps
        self.reto_femoral     = reto_femoral     * self.quadriceps
        return self
