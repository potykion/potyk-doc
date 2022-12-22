import io
from pathlib import Path
from typing import Any, Union

from docxtpl import DocxTemplate


def render_docx_from_template(docx_path: Union[str, Path], **context: Any) -> bytes:
    """
    Рендерит docx из шаблона {docx_path}
    :param docx_path: Путь к docx-шаблону - docx-файл, использующий jinja-like синтаксис согласно `docxtpl <https://docxtpl.readthedocs.io/en/latest/>`_
    :param context: kwargs, которые передаются в шаблон (аналогично тому, как это делается в jinja)
    :return: docx-байты
    """
    doc = DocxTemplate(docx_path)
    doc.render(context)
    doc.save(stream := io.BytesIO())
    return stream.getvalue()
