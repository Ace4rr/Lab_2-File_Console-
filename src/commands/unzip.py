import os
import zipfile
from commands.base_command import BaseCommand
from core.logger import logger

class UnzipCommand(BaseCommand):
    def execute(self,args: list[str]):
        """
        Распаковывает ZIP-архив в текущую директорию

        Args:
            args: список аргументов:
                [archive: путь к .zip файлу]

        Returns:
            None: [распаковывает архив и печатает сообщение в консоль]
        """
        try:
            archive=args[0]
            if not os.path.isfile(archive):
                raise NotADirectoryError("No such file or directory: {archive}")
            if not archive.lower().endswith(".zip"):
                raise ValueError("Not a .zip file")

            with zipfile.ZipFile(archive, "r") as z:
                z.extractall(os.getcwd())
            logger.info(f"unzip {archive}")
            print(f"Unpacked ZIP: {archive}")
        except Exception as e:
            logger.error(f"Error executing unzip: {e}")
            print(f"Error: {e}")
