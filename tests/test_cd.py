import os
from commands.cd import CdCommand

def test_cd_changes_directory(tmp_path, monkeypatch):
    start=os.getcwd()
    CdCommand().execute([str(tmp_path)])
    assert os.getcwd()==str(tmp_path)
    os.chdir(start)
def test_cd_invalid_path(capsys):
    CdCommand().execute(["/no/such/dir"])
    captured=capsys.readouterr()
    assert "Error" in captured.out
