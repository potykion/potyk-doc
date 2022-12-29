import os.path
from pathlib import Path

from potyk_doc.file import this_dir, read_f, read_f_in_this_dir, save_f_in_this_dir


def test_this_dir():
    assert this_dir() == Path(__file__).resolve().parent


def test_read_f():
    with open(this_dir() / 'pdf.html') as f:
        exp_data = f.read()

    assert read_f(this_dir() / 'pdf.html', mode='r') == exp_data


def test_read_f_in_this_dir():
    with open(this_dir() / 'pdf.html') as f:
        exp_data = f.read()

    assert read_f_in_this_dir('pdf.html', mode='r') == exp_data


def test_save_f_in_this_dir():
    if os.path.exists(this_dir() / 'sam.txt'):
        os.remove(this_dir() / 'sam.txt')

    save_f_in_this_dir('sam.txt', b'sam')

    assert read_f_in_this_dir('sam.txt') == b'sam'
    os.remove(this_dir() / 'sam.txt')
