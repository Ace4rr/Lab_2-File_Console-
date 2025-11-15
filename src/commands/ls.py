import os
import stat
import datetime
from commands.base_command import BaseCommand
from core.logger import logger

class LsCommand(BaseCommand):
    def execute(self,args: list[str]):
        try:
            detailed="-l" in args #типа "подробный режим" (указывается размер, дата и тп)
            path=next((a for a in args if not a.startswith("-")),os.getcwd())
            if not os.path.exists(path):
                raise FileNotFoundError(f"No such file or directory: {path}")
            if os.path.isfile(path):
                print(os.path.basename(path))
                logger.info(f"ls {path}")#логирует команду
                return
            entries =sorted(os.listdir(path))#получает список файлов с сортировкой по имени

            if not detailed:
                for entry in entries:
                    print(entry)#если 'l не указан то выводит тупо весь список файлов
            else:
                print(f"{'Mode':<12} {'Size':>10} {'Modified':<20} Name") #эта штука называется форматными строками
                print("-" * 60)
                for entry in entries:
                    full_path =os.path.join(path,entry)
                    stat=os.stat(full_path)#собирает полный путь
                    size=stat.st_size#размер файла
                    mtime=datetime.datetime.fromtimestamp(stat.st_mtime)#время последнего изменения
                    mode=self._get_mode(full_path)#получаем права доступа на файл
                    print(f"{mode:<12} {size:>10} {mtime:%Y-%m-%d %H:%M:%S} {entry}")#вывод форматипрованной строки с инфой о файле
            logger.info(f"ls {''.join(args)} executed succesful")
        except Exception as e:#если в try у нас ошибочка то записываем её в лог и выводим в консоль
            logger.error(f"Error executing ls:{e}")
            print(f"Error:{e}")
    def _get_mode(self,path:str)->str: #отвечает за строку с правами доступа
        mode=os.stat(path).st_mode
        perms="d" if os.path.isdir(path) else "-" #директория или - если это файл
        for who in ["USR","GRP","OTH"]:
            for what in["R","W","X"]:#права пользователей
                flag = getattr(stat, f"S_I{what}{who}")
                perms+=what.lower() if mode & flag else "-"#& потому что тут битовая маска и сравниваем несколько флагов сразу
        return perms
