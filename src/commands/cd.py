import os
from commands.base_command import BaseCommand
from core.logger import logger

class CdCommand(BaseCommand):
    def execute(self, args: list[str]):
        try:
            target = args[0] if args else "~"
            path = os.path.abspath(os.path.expanduser(target))
            if not os.path.isdir(path):
                raise NotADirectoryError(f"No such file or directory: {path}")
            os.chdir(path)
            logger.info(f"cd {path}")
        except Exception as e:
            logger.error(f"Error executing cd:{e}")
            print(f"Error:{e}")
