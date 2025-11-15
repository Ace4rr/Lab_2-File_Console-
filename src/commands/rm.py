import os
import shutil
from commands.base_command import BaseCommand
from core.logger import logger

class RmCommand(BaseCommand):
    def execute(self, args: list[str]):
        try:
            recursive="-r" in args
            path=next((a for a in args if not a.startswith("-")), None)
            if not path:
                raise ValueError("rm requires a target path")
            abs_path= os.path.abspath(os.path.expanduser(path))
            if abs_path in (os.path.abspath("/"), os.path.abspath("..")):
                raise PermissionError("Refusing to remove root or parent directory")
            if not os.path.exists(abs_path):
                raise FileNotFoundError(f"No such file or directory: {abs_path}")
            if os.path.isdir(abs_path):
                if not recursive:
                    raise IsADirectoryError("Use -r to remove directories")

                confirm =input(f"Remove directory '{abs_path}'? [y/N]: ").strip().lower()
                if confirm != "y":
                    print("Cancelled.")
                    return

                shutil.rmtree(abs_path)
                logger.info(f"rm -r {abs_path}")
                print(f"Removed directory: {abs_path}")

            else:
                os.remove(abs_path)
                logger.info(f"rm {abs_path}")
                print(f"Removed file: {abs_path}")

        except Exception as e:
            logger.error(f"Error executing rm: {e}")
            print(f"Error: {e}")
