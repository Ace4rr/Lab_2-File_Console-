from commands.cat import CatCommand
def test_cat_reads_file(tmp_path, capsys):
    file =tmp_path/"test.txt"
    file.write_text("hello world")
    CatCommand().execute([str(file)])
    captured = capsys.readouterr()

    assert "hello world" in captured.out
def test_cat_missing_file(capsys):
    CatCommand().execute(["/no/such/file"])
    captured = capsys.readouterr()
    assert "Error" in captured.out

def test_cat_directory_error(tmp_path, capsys):
    CatCommand().execute([str(tmp_path)])
    captured=capsys.readouterr()
    assert "Is a directory" in captured.out
