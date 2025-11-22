import os
import zipfile
from commands.unzip import UnzipCommand


def test_unzip_extracts_files(tmp_path):
    """Проверка распаковки ZIP-архива"""
    archive=tmp_path / "test.zip"
    with zipfile.ZipFile(archive,"w") as z:
        z.writestr("file1.txt", "data1")
        z.writestr("file2.txt", "data2")
    os.chdir(tmp_path)
    UnzipCommand().execute([str(archive)])
    assert (tmp_path / "file1.txt").exists()
    assert (tmp_path / "file2.txt").exists()
    assert (tmp_path / "file1.txt").read_text() == "data1"

def test_unzip_nested_structure(tmp_path):
    """Проверка распаковки вложенной структуры"""
    archive=tmp_path / "nested.zip"
    with zipfile.ZipFile(archive,"w") as z:
        z.writestr("dir/file.txt", "content")
    os.chdir(tmp_path)
    UnzipCommand().execute([str(archive)])
    assert (tmp_path / "dir" / "file.txt").exists()

def test_unzip_nonexistent_file(tmp_path, capsys):
    """Проверка ошибки при распаковке несуществующего архива"""
    archive=tmp_path / "nonexistent.zip"
    UnzipCommand().execute([str(archive)])
    captured=capsys.readouterr()
    assert "Error" in captured.out

def test_unzip_not_zip_file(tmp_path, capsys):
    """Проверка ошибки при попытке распаковать не-ZIP файл"""
    fake_archive=tmp_path / "fake.txt"
    fake_archive.write_text("not a zip")
    UnzipCommand().execute([str(fake_archive)])
    captured=capsys.readouterr()
    assert "Error" in captured.out
