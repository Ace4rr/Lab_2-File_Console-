
import shlex
from core.argparser import build_parsers
from commands.ls import LsCommand
from commands.cd import CdCommand
from commands.cat import CatCommand
from commands.cp import CpCommand
from commands.mv import MvCommand
from commands.rm import RmCommand

parser=build_parsers()
def main():
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
        except Exception as e:
                print(f"Error:{e}")

if __name__ == "__main__":
    main()
