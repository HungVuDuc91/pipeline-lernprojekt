import sys


def anteil(gesamtkosten: float, flaeche: float, gesamtflaeche: float) -> float:
    """Kostenanteil einer Wohnung nach Wohnfläche, auf Cent gerundet."""
    if gesamtflaeche <= 0:
        raise ValueError("Gesamtfläche muss größer als 0 sein")
    return round(gesamtkosten * flaeche / gesamtflaeche, 2)


if __name__ == "__main__":
    gesamtkosten, flaeche, gesamtflaeche = map(float, sys.argv[1:4])
    print(anteil(gesamtkosten, flaeche, gesamtflaeche))
