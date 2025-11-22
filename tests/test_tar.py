import tarfile
from commands.tar import TarCommand

def test_tar_creates_archive(tmp_path):
    """Проверка создания TAR-архива из директории"""
    folder=tmp_path / "test_folder"
    folder.mkdir()
    (folder / "file1.txt").write_text("content1")
    (folder / "file2.txt").write_text("content2")
    archive=tmp_path / "archive.tar.gz"
    TarCommand().execute([str(folder), str(archive)])
    assert archive.exists()
    with tarfile.open(archive, "r:gz") as tar:
        names=tar.getnames()
        assert any("file1.txt" in n for n in names)
        assert any("file2.txt" in n for n in names)

def test_tar_nested_structure(tmp_path):
    """Проверка упаковки вложенной структуры директорий"""
    folder=tmp_path / "root"
    folder.mkdir()
    subfolder=folder / "sub"
    subfolder.mkdir()
    (folder / "a.txt").write_text("a")
    (subfolder / "b.txt").write_text("b")
    archive=tmp_path / "nested.tar"
    TarCommand().execute([str(folder), str(archive)])
    assert archive.exists()
    with tarfile.open(archive, "r:gz") as tar:
        names=tar.getnames()
        assert any("a.txt" in n for n in names)
        assert any("b.txt" in n for n in names)

def test_tar_nonexistent_folder(tmp_path, capsys):
    """Проверка ошибки при упаковке несуществующей директории"""
    folder=tmp_path / "nonexistent"
    archive=tmp_path / "archive.tar.gz"
    TarCommand().execute([str(folder), str(archive)])

    captured=capsys.readouterr()
    assert "Error" in captured.out


def test_tar_empty_folder(tmp_path):
    """Проверка создания архива из пустой директории"""
    folder=tmp_path / "empty"
    folder.mkdir()
    archive=tmp_path / "empty.tar.gz"
    TarCommand().execute([str(folder),str(archive)])
    assert archive.exists()
