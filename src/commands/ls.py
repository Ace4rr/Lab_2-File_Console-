import os
import stat
import datetime
from commands.base_command import BaseCommand
from core.logger import logger

class LsCommand(BaseCommand):
    """Команда для вывода списка файлов и директорий"""
    def execute(self,args: list[str]):
        """
        Выводит содержимое директории или информацию о файле

        Args:
            args: список аргументов:
                [-l: детальный вывод с правами, размером и датой
                path: путь к файлу или директории]

        Returns:
            None: [печатает список файлов в консоль]
        """

        try:
            detailed="-l" in args
            path=next((a for a in args if not a.startswith("-")),os.getcwd())
            if not os.path.exists(path):
                raise FileNotFoundError(f"No such file or directory: {path}")
            if os.path.isfile(path):
                print(os.path.basename(path))
                logger.info(f"ls {path}")
                return
            entries=sorted(os.listdir(path))

            if not detailed:
                for entry in entries:
                    print(entry)
            else:
                print(f"{'Mode':<12} {'Size':>10} {'Modified':<20} Name")
                print("-" * 60)
                for entry in entries:
                    full_path =os.path.join(path,entry)
                    stat=os.stat(full_path)
                    size=stat.st_size
                    mtime=datetime.datetime.fromtimestamp(stat.st_mtime)
                    mode=self._get_mode(full_path)
                    print(f"{mode:<12} {size:>10} {mtime:%Y-%m-%d %H:%M:%S} {entry}")
            logger.info(f"ls {''.join(args)} executed succesful")
        except Exception as e:
            logger.error(f"Error executing ls:{e}")
            print(f"Error:{e}")
    def _get_mode(self,path:str)->str:
        """
        Возвращает строку с правами доступа в формате Unix

        Args:
            path: путь к файлу или директории

        Returns:
            строка типа 'drwxr-xr-x' или '-rw-r--r--'
        """
        mode=os.stat(path).st_mode
        perms="d" if os.path.isdir(path) else "-"
        for who in ["USR","GRP","OTH"]:
            for what in["R","W","X"]:
                flag = getattr(stat, f"S_I{what}{who}")
                perms+=what.lower() if mode & flag else "-"
        return perms
