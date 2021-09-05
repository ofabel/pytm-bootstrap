from tarfile import open
from tempfile import TemporaryFile


class Archiver:
    def __init__(self, base_path: str):
        self._base_path: str = base_path

    def create_tar(self) -> bytes:
        with TemporaryFile() as temp_archive:
            with open(mode='w|gz', fileobj=temp_archive) as tar:
                tar.add('/home/ofa/dev/ibre/python-tool-example/app.py')
                temp_archive.seek(0)
                return temp_archive.read()
