import os
from commands.base_command import BaseCommand
from core.logger import logger

class CatCommand(BaseCommand):
    def execute(self, args: list[str]):
        try:


            target=args[0]
            path = os.path.abspath(os.path.expanduser(target))
            if not path:
                raise ValueError("rm requires a target path")
            if not os.path.exists(path):
                raise FileNotFoundError(f"No such file or directory: {path}")
            if os.path.isdir(path):
                raise NotADirectoryError(f"cat:{path}:Is a directory")
            with open(path,"r",encoding="utf-8") as f:
                print(f.read())
            logger.info(f"cat {path}")
        except Exception as e:
            logger.error(f"cat error:{e}")
            print(f"Error:{e}")
