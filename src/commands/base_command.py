from abc import ABC, abstractmethod

class BaseCommand(ABC):#делаем абстрактные классы чтобы можно было по универсальному вызывать команды
    @abstractmethod
    def execute(self, args: list[str]):
        pass
