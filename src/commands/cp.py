import os
import shutil
from commands.base_command import BaseCommand
from core.logger import logger

class CpCommand(BaseCommand):
    """Команда для копирования файлов и директорий"""
    def execute(self, args: list[str]):
        """
        Копирует файлы или директории

        Args:
            args: список аргументов ["-r", "source", "destination"]
                  -r: рекурсивное копирование для директорий

        Returns:
            None: [копирует файлы или директории в укаханное место]
        """
        try:
            recursive = "-r" in args
            if recursive:
                args.remove("-r")

            if len(args) < 2:
                raise ValueError("cp requires source and destination paths")

            src, dst = args

            src_path = os.path.abspath(os.path.expanduser(src))
            dst_path = os.path.abspath(os.path.expanduser(dst))

            if not os.path.exists(src_path):
                raise FileNotFoundError(f"No such file or directory: {src_path}")

            if os.path.isdir(src_path):
                if not recursive:
                    raise IsADirectoryError("Use -r to copy directories")
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            else:
                shutil.copy2(src_path, dst_path)

            logger.info(f"cp {' '.join(args)}")
            print(f"Copied {src} -> {dst}")

        except Exception as e:
            logger.error(f"Error executing cp: {e}")
            print(f"Error: {e}")
