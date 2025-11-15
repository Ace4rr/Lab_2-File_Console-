from abc import ABC, abstractmethod

class BaseCommand(ABC):
    """Создание абстрактного класса"""
    @abstractmethod
    def execute(self, args: list[str]):
        pass
