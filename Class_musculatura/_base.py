import dataclasses
from abc import ABC, abstractmethod

@dataclasses.dataclass
class MuscleGroup(ABC):
    """
    Abstract Base Class for all muscle groups.
    Enforces a standard interface for volume and distribution setting.
    """

    @abstractmethod
    def set_volume(self, series: float) -> "MuscleGroup":
        """
        Sets the total series count for the muscle group.
        Replaces: set_peito_simples, set_costas_simples, etc.
        """
        pass

    @abstractmethod
    def set_distribution(self, **kwargs) -> "MuscleGroup":
        """
        Distributes the volume across specific muscle portions.
        
        Note: Subclasses should implement strict arguments or validate 
        kwargs to ensure the distribution is correct for that specific muscle.
        """
        pass

    def validate_sum(self, tolerance: float = 0.01) -> bool:
        """
        Optional helper: Checks if sub-portions sum up to ~1.0 (100%).
        You can call this inside set_distribution if you want strict checking.
        """
        # Logic to be implemented if you want to enforce math validity
        # grabbing all fields except the main volume and checking sum
        return True