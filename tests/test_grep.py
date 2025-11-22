from commands.grep import GrepCommand

def test_grep_simple(tmp_path, capsys):
    f=tmp_path/"a.txt"
    f.write_text("hello\nworld\nHELLO")
    GrepCommand().execute(["hello",str(f)])
    captured=capsys.readouterr()
    assert "hello" in captured.out


def test_grep_ignore_case(tmp_path, capsys):
    f=tmp_path / "a.txt"
    f.write_text("HELLO")
    GrepCommand().execute(["hello", str(f),"-i"])
    captured=capsys.readouterr()
    assert "HELLO" in captured.out


def test_grep_directory_without_r(tmp_path,capsys):
    d = tmp_path / "dir"
    d.mkdir()

    GrepCommand().execute(["abc", str(d)])
    captured=capsys.readouterr()

    assert "Directory requires -r option" in captured.out


def test_grep_recursive(tmp_path, capsys):
    d=tmp_path / "dir"
    d.mkdir()
    f=d / "file.txt"
    f.write_text("abc")

    GrepCommand().execute(["abc", str(d), "-r"])
    captured = capsys.readouterr()

    assert "file.txt" in captured.out
