# Miinaharava
Miinaharava-peli. Tarkoitus käyttää logiikka ja vähän onnea ja etsiä kaikki miinat. Varo jännetuppitulehdusta.  

## Dokumentaatio

[vaatimusmäärittely](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

## Asennus
Asenna [python3](https://realpython.com/installing-python/), [pip](https://pip.pypa.io/en/stable/installing/) ja [poetry](https://python-poetry.org/docs/).
Käytä komentoja 
```
python3
```
```
pip3
```
Etsi pelin hakemisto ja aja komento
```
poetry install
```
Peli käynnistyy
```
poetry run invoke start
```
Testikattavuusraportti
```
poetry run invoke coverage
poetry run invoke coverage-report
```
#### Yliopiston koneella
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
```
muokkaa pyproject.toml tiedostoon pythonin versioksi 3.6
```
poetry run invoke start
```
## Log
Ohjeissa sanotaan, että README siistinä, mutta pidän tämän osion toistaiseksi. Helpotta huomattavasti projektin seuraamista.
### viikko3
-Poistin viikko 2 tehtävät, koska aiheuttivat ongelmia testien kanssa. Ovat vielä tallessa, mutta deadlinen lähestyessä korjaan ongelmat myöhemmin(tarvittaessa?).

-Koodin pohja valmis. Tehty tkinterillä. Ruudut ovat nappuloita ja klikatessa kertovat onko ruutu miina(M) tai numeron montako miinaa lähellä. Vielä ei mitään endgame ruutuja, eli käyttäjän vastuulla epäonnistuminen ja onnistuminen. Koko on 10x10 ja miinoja 10. Laskurit eivät vielä toimi. Liputtaminen mahdollista oikealla painikkeella.
### viikko4
-endgame-popup

-0-ruutua painettaessa automattisesti avaa koko alueen.

-pixilart.com hyödyntäen kuvat ruutuja varten.

-miinalaskuri
