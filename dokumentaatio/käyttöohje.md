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
### Peli käynnistyy.
```
poetry run invoke start
```
### Testikattavuusraportti.
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

## Pelin käyttöohje
Peli avautuu pelinäkymään:

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Kiinni.png">

Ruutuja voi avata klikkaamalla. Avatussa ruudussa oleva numero kertoo kuinka monta miinaa on viereisissä ruuduissa. Miinoja voi merkitä lipulla käyttämällä hiiren oikeaa painiketta. Jos numeron ympäriltä on liputettu sen arvon verran ruutuja, voit tuplaklikkaamalla ruutua avata kaikki vielä kiinni olevat ruudut.

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Avattu.png">

Painamalla pelinäkymän vasemmasta yläkulmasta menu ja sitten settings avautuu asetusnäkymä.
Asetusnäkymästä voi valita ruudun koon ja miinojen määrän valmiista vaihtoehdoista tai syöttää itse valitsemansa arvot oikella olevaan custom kohtaan.

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Settings.png">

Painamalla miinasta häviät pelin. Jos olet liputtanut ruutuja väärin, ne ovat pelin lopussa näkyvissä punaisella X merkinnällä. 

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Häviö.png">

Voitat pelin avaamalla kaikki ruudut, joissa ei ole miinaa.  

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Voitto.png">
