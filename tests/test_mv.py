from commands.mv import MvCommand

def test_mv_moves_file(tmp_path, capsys):
    """Проверка перемещения файла"""
    src=tmp_path/"s.txt"
    dst=tmp_path/"d.txt"
    src.write_text("hello")
    MvCommand().execute([str(src), str(dst)])
    assert not src.exists()
    assert dst.exists()
    assert dst.read_text() =="hello"
def test_mv_invalid_src(capsys):
    """Проверка обработки несуществующего источника"""
    MvCommand().execute(["/no/such/file", "/tmp/x"])
    captured=capsys.readouterr()

    assert "Error" in captured.out
