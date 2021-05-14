# Testausdokumentti
Ohjelman logiikka testataan automaattisin testein. Käyttöliittymään liittyvä testaus on suoritettu manuaalisesti.

## Automaattiset testit

Koska käyttöliittymää ei oteta huomioon, on testikattavuus 99%. 
<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/test_coverage.png">

### Square
Square luokka on hyvin yksinkertainen, joten sitä testaava TestSquare luokka tekee yhden testin. Testissä testataan luokan string-tulostusta. 

### MSGrid
MSGrid luokkaa testaa TestMSGrid luokka. Testeissä hyödynnetään paljon luokan string-tulostusta. Random- kirjastoa hyödyntävien metodien testauksessa on määritelty aluksi seed(). Testaustulokset on siten saatu vain kokeilemalla. 

### Settings
Settings luokkaa testaa TestSettings. Settings luokan tarkoitus on käsitellä tiedostoa. Testeissä luodaan settings_test.csv tiedosto data hakemistoon. Jokainen testi poistaa tiedoston ennen assert-komentoja. Tiedoston luomisella on tarkoitus testata luokan toimintaa vaikuttamatta tällä hetkellä tallennettuihin tietoihin. Sovelluksen tiedostojen nimet on määritelty config.py tiedostossa. Mikäli käyttäjä valitsee tiedostonimeksi settings_test.csv tulevat testit vaikuttamaan sovelluksen käyttöön.

### Statistics
Statistics luokka myös käsittelee tiedostoa, kuten Settings. Statistics luokan testauksessa on samat periatteet. Testit luovat statistics_test.csv tiedoston ja poistavat sen ennen assert-komentoja. Mikäli nimi on määritelty samaksi config.py tiedostossa, vaikuttaa testit tallennettuihin tietoihin. Tässä merkitys on keskeisempi, koska testien ajaminen pyyhkisi pelitilastot.

## Käyttöliittymä
Käyttöliittymää on testattu manuaalisesti pelaamalla peliä. Testaamiseen käytetystä ajasta ei ole arviota, koska aktiivisen testauksen ja rennon pelaamisen eroa ei kyetty havannoimaan. 

Testeissä on havaittu, että rämppäämällä voi saada klikkauksen rekisteröitymään useamman kerran. Tällä hetkellä sovellus määrittää pelin voittamisen klikkausten määrän mukaan, joten pelin voitto viesti tulee joko liian aikaisin tai sitä ei tule ollenkaan. Klikkausten määrä siis kasvaa liian nopeasti ja huonossa tapauksessa menee yli voittomäärästä. Korjaus on lopetuskonditioiden siirto pelilogiikan puolella, jossain vaiheessa.

Peliä avatessa ja pelin ruudukkokokoa vaihtaessa ensimmäinen piirto välillä kestää pitkään. Ajastamalla GameUI luokan reset metodin eri vaiheita, voidaan sanoa että syy lienee olla tkinter kirjastossa. Vaiheiden kestojen summa pysyy alle 0.5 sekunnissa, mutta piirron näkymiseen voi kestää yli 2 sekuntia. Korjauksesta ei tietoa. Pelin resetointi pysyessä samalla ruudukkokoolla ja avauksen jälkeen on kuitenkin nopea.
