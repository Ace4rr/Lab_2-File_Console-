import os
import tarfile
from commands.base_command import BaseCommand
from core.logger import logger

class TarCommand(BaseCommand):
    def execute(self,args: list[str]):
        """
        Создаёт TAR-архив из указанной директории

        Args:
            args: список аргументов:
                [folder: путь к директории для упаковки
                archive: имя выходного tar-архива]

        Returns:
            None: [создаёт TAR-архив и печатает сообщение в консоль]
        """
        try:
            folder,archive=args
            folder=os.path.abspath(folder)
            archive=os.path.abspath(archive)
            if not os.path.isdir(folder):
                raise NotADirectoryError("No such file or directory: {folder}")

            with tarfile.open(archive, "w:gz") as tar:
                tar.add(folder,arcname=os.path.basename(folder))
            logger.info(f"tar{folder} {archive}")
            print(f"Created TAR: {archive}")
        except Exception as e:
            logger.error(f"Error executing tar: {e}")
            print(f"Error: {e}")
