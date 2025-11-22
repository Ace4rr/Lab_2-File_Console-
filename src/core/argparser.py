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

    p_grep = subparsers.add_parser("grep")
    p_grep.add_argument("-r", action="store_true")
    p_grep.add_argument("-i", action="store_true")
    p_grep.add_argument("pattern")
    p_grep.add_argument("path")

    p_zip = subparsers.add_parser("zip")
    p_zip.add_argument("folder")
    p_zip.add_argument("archive")

    p_unzip = subparsers.add_parser("unzip")
    p_unzip.add_argument("archive")

    p_tar = subparsers.add_parser("tar")
    p_tar.add_argument("folder")
    p_tar.add_argument("archive")

    p_untar = subparsers.add_parser("untar")
    p_untar.add_argument("archive")

    return parser
