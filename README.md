# Miinaharava
Miinaharava-peli. Tarkoitus käyttää logiikka ja vähän onnea ja etsiä kaikki miinat. Varo jännetuppitulehdusta.  

## Dokumentaatio

[vaatimusmäärittely](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[käyttöohje](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

[release](https://github.com/ElomaaTapio/ot-harjoitustyo/releases)

## Asennus
Asenna [python3](https://realpython.com/installing-python/), [pip](https://pip.pypa.io/en/stable/installing/) ja [poetry](https://python-poetry.org/docs/).
Käytä komentoja.
```
python3
```
```
pip3
```
Etsi pelin hakemisto ja aja komento.
```
poetry install
```
Peli käynnistyy.
```
poetry run invoke start
```
Testikattavuusraportti.
```
poetry run invoke coverage
poetry run invoke coverage-report
```
### Yliopiston koneella
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
```
Muokkaa pyproject.toml tiedostoon pythonin versioksi 3.6.
Pelin hakemistossa.
```
poetry install
poetry run invoke start
```
