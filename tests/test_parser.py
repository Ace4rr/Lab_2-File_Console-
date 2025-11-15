import shlex
from core.argparser import build_parsers

def test_parse_ls():
    parser =build_parsers()
    args=parser.parse_args(shlex.split("ls -l /tmp"))
    assert args.command == "ls"
    assert args.l is True
    assert args.path == "/tmp"

def test_parse_cp():
    parser=build_parsers()
    args=parser.parse_args(shlex.split("cp -r a b"))
    assert args.command == "cp"
    assert args.r is True
    assert args.src == "a"
    assert args.dst == "b"
def test_parse_rm_no_r():
    parser=build_parsers()
    args=parser.parse_args(shlex.split("rm file.txt"))
    assert args.command == "rm"
    assert args.r is False
    assert args.path == "file.txt"
