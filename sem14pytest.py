import pytest
from sem14 import del_other_symbol


def test_is_true():
    assert del_other_symbol('wew wefefe') == 'wew wefefe'


def test_lower():
    assert del_other_symbol('wew wefeFE') == 'wew wefefe'


def test_punkt():
    assert del_other_symbol('wew _wefefe,.:;') == 'wew wefefe'


def test_kirill():
    assert del_other_symbol('wew _wыавываefefe,.:;') == 'wew wefefe'


def test_komplex():
    assert del_other_symbol('Wew _wыавываefefe,.:;') == 'wew wefefe'


if __name__ == '__main__':
    pytest.main(['-v'])
