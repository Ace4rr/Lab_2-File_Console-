import zipfile
from commands.zip import ZipCommand


def test_zip_creates_archive(tmp_path):
    """Проверка создания ZIP-архива из директории"""
    folder=tmp_path / "test_folder"
    folder.mkdir()
    (folder / "file1.txt").write_text("content1")
    (folder / "file2.txt").write_text("content2")

    archive=tmp_path / "archive.zip"
    ZipCommand().execute([str(folder), str(archive)])
    assert archive.exists()
    with zipfile.ZipFile(archive, "r") as z:
        names=z.namelist()
        assert "file1.txt" in names
        assert "file2.txt" in names


def test_zip_nested_structure(tmp_path):
    """Проверка упаковки вложенной структуры директорий"""
    folder=tmp_path / "root"
    folder.mkdir()
    subfolder=folder / "sub"
    subfolder.mkdir()
    (folder / "a.txt").write_text("a")
    (subfolder / "b.txt").write_text("b")

    archive=tmp_path / "nested.zip"
    ZipCommand().execute([str(folder),str(archive)])
    assert archive.exists()
    with zipfile.ZipFile(archive, "r") as z:
        names=z.namelist()
        assert "a.txt" in names
        assert "sub/b.txt" in names or "sub\\b.txt" in names


def test_zip_nonexistent_folder(tmp_path, capsys):
    """Проверка ошибки при упаковке несуществующей директории"""
    folder=tmp_path / "nonexistent"
    archive=tmp_path / "archive.zip"
    ZipCommand().execute([str(folder), str(archive)])
    captured=capsys.readouterr()
    assert "Error" in captured.out


def test_zip_empty_folder(tmp_path):
    """Проверка создания архива из пустой директории"""
    folder=tmp_path / "empty"
    folder.mkdir()
    archive=tmp_path / "empty.zip"
    ZipCommand().execute([str(folder),str(archive)])
    assert archive.exists()
    with zipfile.ZipFile(archive, "r") as z:
        assert len(z.namelist()) == 0
