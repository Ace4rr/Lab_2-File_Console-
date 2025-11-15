from commands.cp import CpCommand


def test_cp_file_to_file(tmp_path, capsys):
    src = tmp_path/"a.txt"
    dst = tmp_path/"b.txt"
    src.write_text("123")
    CpCommand().execute([str(src), str(dst)])
    assert dst.exists()
    assert dst.read_text() == "123"
def test_cp_dir_without_r(tmp_path, capsys):
    src = tmp_path/"folder"
    src.mkdir()
    (src /"f.txt").write_text("abc")
    CpCommand().execute([str(src), str(tmp_path/'copy')])
    captured =capsys.readouterr()

    assert "Use -r" in captured.out

def test_cp_dir_with_r(tmp_path):
    src=tmp_path/"folder"
    dst=tmp_path/"copy"
    src.mkdir()
    (src/"a.txt").write_text("text")
    CpCommand().execute(["-r", str(src), str(dst)])
    assert (dst/"a.txt").exists()
