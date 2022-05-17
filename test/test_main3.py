import sys

path_to_module = "/Prog_Modular/temp/"
sys.path.append(path_to_module)
import main3


def test_add():
    assert main.add(3, 4) == 7
    assert main.add(3.5, 4) == 7
    assert main.add(3.9, 4) == 7
    assert main.add(3.9, 4.1) == 8


def test_to_sentence():
    assert main.to_sentence('apple') == 'Apple.'
    assert main.to_sentence('Apple trees') == 'Apple trees.'
    assert main.to_sentence('Apple trees.') == 'Apple trees.'
