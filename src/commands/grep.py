import os
import re
from commands.base_command import BaseCommand
from core.logger import logger

class GrepCommand(BaseCommand):
    def execute(self,args: list[str]):
        """
        Выполняет поиск текста в файле по заданному шаблону

        Args:
            args: список аргументов:
                [-r: рекурсивный поиск по каталогам
                -i: поиск без учёта регистра
                pattern: строка для поиска
                path: путь к файлу или директории]

        Returns:
            None: [печатает найденное в консоль]
        """
        try:
            recursive="-r" in args
            ignore_case="-i" in args
            plain=[a for a in args if not a.startswith("-")]
            if len(plain) < 2:
                raise ValueError("Usage: grep <pattern> <path>")
            pattern,path=plain
            path=os.path.abspath(os.path.expanduser(path))
            flags=re.IGNORECASE if ignore_case else 0
            regex=re.compile(pattern, flags)
            if os.path.isfile(path):
                self._search_file(path,regex)
            elif os.path.isdir(path):
                if recursive:
                    for root, _,files in os.walk(path):
                        for f in files:
                            self._search_file(os.path.join(root,f),regex)
                else:
                    raise IsADirectoryError("Directory requires -r option")
            else:
                raise FileNotFoundError(f"No such file or directory: {path}")
            logger.info(f"grep {pattern} {path} -r={recursive} -i={ignore_case}")

        except Exception as e:
            logger.error(f"Error executing grep:{e}")
            print(f"Error: {e}")

    def _search_file(self, file_path, regex):
        try:
            with open(file_path, "r", errors="ignore") as f:
                for num, line in enumerate(f, start=1):
                    if regex.search(line):
                        print(f"{file_path}:{num}: {line.rstrip()}")
        except Exception:
            pass
