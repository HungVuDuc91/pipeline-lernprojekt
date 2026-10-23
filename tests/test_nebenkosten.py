import pytest

from nebenkosten import anteil


def test_anteil_normal():
    assert anteil(1000, 50, 200) == 250.00


def test_anteil_rundet_auf_cent():
    assert anteil(100, 1, 3) == 33.33


def test_gesamtflaeche_null_wirft_fehler():
    with pytest.raises(ValueError):
        anteil(100, 50, 0)