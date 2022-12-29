from potyk_doc.docx import docxs_are_equal
from potyk_doc.file import this_dir


def test_docxs_are_equal():
    with open(this_dir() / 'hey.docx', 'rb') as f:
        docx_1 = docx_2 = f.read()

    assert docxs_are_equal(docx_1, docx_2)
