import os
import tarfile
from commands.base_command import BaseCommand
from core.logger import logger

class UntarCommand(BaseCommand):
    def execute(self,args: list[str]):
        """
        Распаковывает TAR-архив в текущую директорию

        Args:
            args: список аргументов:
                [archive: путь к .tar или .tar.gz файлу]

        Returns:
            None: [распаковывает архив и печатает сообщение в консоль]
        """
        try:
            archive=args[0]
            archive=os.path.abspath(archive)
            if not os.path.isfile(archive):
                raise FileNotFoundError(f"No such file or directory: {archive}")
            if not (archive.lower().endswith(".tar") or archive.lower().endswith(".tar.gz")):
                raise ValueError("Not a .tar file")
            with tarfile.open(archive, "r:*") as tar:
                tar.extractall()
            logger.info(f"untar {archive}")
            print(f"Unpacked TAR: {archive}")
        except Exception as e:
            logger.error(f"Error executing untar: {e}")
            print(f"Error: {e}")
