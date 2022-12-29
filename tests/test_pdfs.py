import io
import shutil
from pathlib import Path

import PyPDF2
import pytest

from potyk_doc.file import this_dir
from potyk_doc.pdf import render_pdf_from_html, pdfs_are_equal


@pytest.mark.skipif(shutil.which('wkhtmltopdf') is None, reason='wkhtmltopdf не установлен')
def test_render_pdf_from_html():
    with open(this_dir() / 'pdf.html') as f:
        html = f.read()

    pdf = render_pdf_from_html(html)

    assert PyPDF2.PdfReader(io.BytesIO(pdf)).pages[0].extract_text() == 'hey'


@pytest.mark.skipif(shutil.which('wkhtmltopdf') is None, reason='wkhtmltopdf не установлен')
def test_pdfs_are_equal():
    with open(this_dir() / 'pdf.html') as f:
        html = f.read()
    pdf_1 = render_pdf_from_html(html)
    pdf_2 = render_pdf_from_html(html)

    assert pdfs_are_equal(pdf_1, pdf_2)
