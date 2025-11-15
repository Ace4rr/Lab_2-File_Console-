from commands.rm import RmCommand

def test_rm_file(tmp_path):
    """Проверка удаления файла"""
    file =tmp_path / "a.txt"
    file.write_text("x")
    RmCommand().execute([str(file)])
    assert not file.exists()
def test_rm_dir_requires_r(tmp_path, capsys):
    """Проверка удаления директории без флага -r"""
    folder=tmp_path/"dir"
    folder.mkdir()
    RmCommand().execute([str(folder)])
    captured=capsys.readouterr()
    assert "Use -r" in captured.out
def test_rm_dir_with_confirmation(tmp_path, monkeypatch):#используем monketpatch чтобы имитировать ввод
    """Проверка удаления директории с подтверждением"""
    folder=tmp_path/"dir"
    folder.mkdir()
    (folder/ "a.txt").write_text("123")
    monkeypatch.setattr("builtins.input", lambda _: "y")
    RmCommand().execute(["-r",str(folder)])
    assert not folder.exists()
def test_rm_cancel(tmp_path, monkeypatch, capsys):
    """Проверка отмены удаления директории"""
    folder= tmp_path/"dir"
    folder.mkdir()
    monkeypatch.setattr("builtins.input",lambda _:"n")
    RmCommand().execute(["-r", str(folder)])
    assert folder.exists()
    captured = capsys.readouterr()
    assert "Cancelled" in captured.out
