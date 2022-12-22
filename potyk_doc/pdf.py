import dataclasses
from pathlib import Path
from typing import Dict, Union

import pdfkit

from potyk_doc.models import File, FileName, HTMLStr


@dataclasses.dataclass()
class WkhtmltopdfOptions:
    """
    >>> WkhtmltopdfOptions().page_width('209.804').page_height("296.926").options
    {'--page-width': '209.804', '--page-height': '296.926'}
    """
    options: Dict[str, str] = dataclasses.field(default_factory=dict)

    def add_option(self, option_name, option_val):
        return dataclasses.replace(self, options={**self.options, option_name: option_val})

    def page_width(self, page_width_mm: str):
        return self.add_option('--page-width', page_width_mm)

    def page_height(self, page_height_mm: str):
        return self.add_option('--page-height', page_height_mm)

    def footer_html(self, footer_html_path: str):
        return self.add_option("--footer-html", footer_html_path)

    def header_html(self, header_html_path: str):
        return self.add_option("--header-html", header_html_path)


def render_pdf_from_html(
    pdf_html: HTMLStr,
    pdf_name: FileName,
    css_path: Union[str, Path, None] = None,
    options: Union[dict, WkhtmltopdfOptions, None] = None,
) -> File:
    """
    Рендерит pdf из html {pdf_html}.
    Рендер происходит с помощью либы pdfkit,
    которая в свою очередь использует `wkhtmltopdf <https://wkhtmltopdf.org/>`_ (=> она должна быть установлена)

    :param pdf_html: HTML-строка
    :param pdf_name: Название pdf-файла
    :param css_path: (опционально) путь к css-файлу, в котором будут стили, применяемые к html перед рендерингом
    :param options: (опционально) Словарь опций wkhtmltopdf, напр. {"--page-width": "209.804"}
    :return: File с pdf-байтами и названием {pdf_name}
    """
    options = options.options if isinstance(options, WkhtmltopdfOptions) else options
    pdf_data = pdfkit.from_string(pdf_html, False, css=css_path, options=options)
    return File(pdf_data, pdf_name)
