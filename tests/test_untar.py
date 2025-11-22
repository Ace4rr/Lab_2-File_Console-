import os
import tarfile
from commands.untar import UntarCommand

def test_untar_extracts_files(tmp_path):
    """Проверка распаковки TARархива"""
    folder=tmp_path / "source"
    folder.mkdir()
    (folder / "file1.txt").write_text("data1")
    (folder / "file2.txt").write_text("data2")
    archive=tmp_path / "test.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(str(folder / "file1.txt"), arcname="source/file1.txt")
        tar.add(str(folder / "file2.txt"), arcname="source/file2.txt")
    extract_dir=tmp_path / "extract"
    extract_dir.mkdir()
    os.chdir(extract_dir)
    UntarCommand().execute([str(archive)])
    assert (extract_dir / "source" / "file1.txt").exists()
    assert (extract_dir / "source" / "file2.txt").exists()

def test_untar_nonexistent_file(tmp_path, capsys):
    """Проверка ошибки при распаковке несуществующего архива"""
    archive=tmp_path / "nonexistent.tar.gz"
    UntarCommand().execute([str(archive)])
    captured=capsys.readouterr()
    assert "Error" in captured.out


def test_untar_not_tar_file(tmp_path, capsys):
    """Проверка ошибки при попытке распаковать не TAR файл"""
    fake_archive=tmp_path / "fake.txt"
    fake_archive.write_text("not a tar")
    UntarCommand().execute([str(fake_archive)])
    captured=capsys.readouterr()
    assert "Error" in captured.out
