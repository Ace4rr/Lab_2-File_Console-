import argparse

def build_parsers():
    parser=argparse.ArgumentParser(prog="",add_help=False)
    subparsers=parser.add_subparsers(dest=("command"))
    p_ls = subparsers.add_parser("ls")
    p_ls.add_argument("-l", action="store_true")
    p_ls.add_argument("path", nargs="?", default=".")

    p_cd = subparsers.add_parser("cd")
    p_cd.add_argument("path", nargs="?", default="~")
    p_cat = subparsers.add_parser("cat",add_help=False)
    p_cat.add_argument("path")

    p_cp = subparsers.add_parser("cp", add_help=False)
    p_cp.add_argument("-r", action="store_true")
    p_cp.add_argument("src")
    p_cp.add_argument("dst")

    p_mv = subparsers.add_parser("mv", add_help=False)
    p_mv.add_argument("src", help="исходный файл или каталог")
    p_mv.add_argument("dst", help="новое имя или путь назначения")

    p_rm = subparsers.add_parser("rm", add_help=False)
    p_rm.add_argument("-r", action="store_true")
    p_rm.add_argument("path")

    return parser
