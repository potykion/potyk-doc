from typing import List

from potyk_doc.models import File
from potyk_doc.zip_ import zip_files, list_zip_files


def test_zip_files():
    files: List[File] = [
        (b'sam1', 'sam1.txt'),
        (b'sam2', 'sam2.txt'),
    ]

    zip_data, zip_name = zip_files(files, 'archive.zip')
    # with open(zip_name, 'wb', ) as f:
    #     f.write(zip_data)

    assert list_zip_files(zip_data) == files
