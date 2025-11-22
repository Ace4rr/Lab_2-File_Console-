import os
import zipfile
from commands.base_command import BaseCommand
from core.logger import logger

class ZipCommand(BaseCommand):
    def execute(self,args: list[str]):
        """
        Создаёт ZIP-архив из указанной директории

        Args:
            args: список аргументов:
                [folder: путь к папке которую нужно упаковать
                archive: имя выходного ZIP-архива]

        Returns:
            None: [создаёт ZIP-архив и печатает сообщение в консоль]
        """

        try:
            folder,archive=args
            folder=os.path.abspath(folder)
            archive=os.path.abspath(archive)
            if not os.path.isdir(folder):
                raise NotADirectoryError("No such file or directory: {folder}")

            with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED) as z:
                for root, _, files in os.walk(folder):
                    for f in files:
                        path=os.path.join(root, f)
                        arcname=os.path.relpath(path, folder)
                        z.write(path, arcname)
            logger.info(f"zip {folder} {archive}")
            print(f"Created ZIP: {archive}")
        except Exception as e:
            logger.error(f"Error executing zip: {e}")
            print(f"Error: {e}")
