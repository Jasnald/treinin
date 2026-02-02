print("Pacote Class_Musculatura iniciado!")

from .adutores            import Adutores
from .bracos              import Triceps, Antebraco, Biceps
from .core                import Abdomen, Lombar
from .costas              import Costas
from .flexores_quadril    import FlexoresDoQuadril
from .gluteo              import Gluteo
from .manguito            import Manguito
from .panturrilha         import Panturrilha
from .peito               import Peito, Ombro
from .posterior           import PosteriorCoxa
from .quadriceps          import Quadriceps
from ._base               import MuscleGroup

__all__ = [
    "MuscleGroup",
    "Peito",
    "Costas",
    "Ombro",
    "Manguito",
    "Antebraco",
    "Triceps",
    "Biceps",
    "Abdomen",
    "Lombar",
    "Adutores",
    "FlexoresDoQuadril",
    "Gluteo",
    "PosteriorCoxa",
    "Quadriceps",
    "Panturrilha",
]
