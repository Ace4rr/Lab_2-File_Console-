from commands.ls import LsCommand

def test_ls_lists_files(tmp_path, capsys):
    (tmp_path/"a.txt").write_text("1")
    (tmp_path/"b.txt").write_text("2")
    LsCommand().execute([str(tmp_path)])
    output=capsys.readouterr().out
    assert "a.txt" in output
    assert "b.txt" in output
def test_ls_single_file(tmp_path, capsys):
    file=tmp_path / "a.txt"
    file.write_text("HELLO")
    LsCommand().execute([str(file)])
    output = capsys.readouterr().out
    assert "a.txt" in output

def test_ls_nonexistent_path(capsys):
    LsCommand().execute(["/no/such/path"])
    output = capsys.readouterr().out
    assert "Error" in output
