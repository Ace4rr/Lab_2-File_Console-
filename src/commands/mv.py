import os
import shutil
from commands.base_command import BaseCommand
from core.logger import logger

class MvCommand(BaseCommand):
    """Команда для перемещения или переименования файлов и директорий"""
    def execute(self, args: list[str]):
        """
        Перемещает или переименовывает файл/директорию

        Args:
            args: список аргументов
                args[0] - исходный путь
                args[1] - путь назначения

         Returns:
            None: [перемещает или переименовывает файл/директорию, выводит результат в консоль]
        """
        try:
            if len(args) < 2:
                raise ValueError("mv requires source and destination")

            src, dst = args
            src_path = os.path.abspath(os.path.expanduser(src))
            dst_path = os.path.abspath(os.path.expanduser(dst))

            if not os.path.exists(src_path):
                raise FileNotFoundError(f"No such file or directory: {src_path}")

            shutil.move(src_path, dst_path)
            logger.info(f"mv {src_path} -> {dst_path}")
            print(f"Moved {src} -> {dst}")

        except Exception as e:
            logger.error(f"Error executing mv: {e}")
            print(f"Error: {e}")
