
import shlex
from core.argparser import build_parsers
from commands.ls import LsCommand
from commands.cd import CdCommand
from commands.cat import CatCommand
from commands.cp import CpCommand
from commands.mv import MvCommand
from commands.rm import RmCommand
from commands.grep import GrepCommand
from commands.zip import ZipCommand
from commands.tar import TarCommand
from commands.unzip import UnzipCommand
from commands.untar import UntarCommand

parser=build_parsers()
def main():
    """REPL цикл для minishell
    Считывает команды пользователя, разбирает их через argparse
    и передаёт выполнение обработчикам"""
    while True:
        raw=input("minishell>")
        if (raw.lower()=="exit") or (raw.lower()==("quit")):
            break
        try:
            args=parser.parse_args(shlex.split(raw, posix=False))
            if  args.command=="ls":
                cmd_args=[]
                if args.l:
                    cmd_args.append("-l")
                cmd_args.append(args.path)
                LsCommand().execute(cmd_args)
            elif  args.command=="cd":
                cmd_args=[]
                cmd_args.append(args.path)
                CdCommand().execute(cmd_args)
            elif args.command=="cat":
                cmd_args=[]
                cmd_args.append(args.path)
                CatCommand().execute(cmd_args)
            elif args.command=="cp":
                cmd_args=[]
                if args.r:
                    cmd_args.append("-r")
                cmd_args.extend([args.src, args.dst])
                CpCommand().execute(cmd_args)
            elif args.command=="mv":
                cmd_args=[]
                cmd_args.extend([args.src, args.dst])
                MvCommand().execute(cmd_args)
            elif  args.command=="rm":
                cmd_args=[]
                if args.r:
                    cmd_args.append("-r")
                cmd_args.append(args.path)
                RmCommand().execute(cmd_args)
            elif args.command==("grep"):
                cmd_args=[]
                if args.r:
                    cmd_args.append("-r")
                if args.i:
                    cmd_args.append("-i")
                cmd_args.extend([args.pattern,args.path])
                GrepCommand().execute(cmd_args)
            elif args.command == "zip":
                ZipCommand().execute([args.folder, args.archive])
            elif args.command == "tar":
                TarCommand().execute([args.folder, args.archive])
            elif args.command == "unzip":
                UnzipCommand().execute([args.archive])
            elif args.command == "untar":
                UntarCommand().execute([args.folder, args.archive])

        except Exception as e:
                print(f"Error:{e}")

if __name__ == "__main__":
    main()
