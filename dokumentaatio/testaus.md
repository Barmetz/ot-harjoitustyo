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
Statistics luokka myös käsittelee tiedostoa, kuten Settings. Statistics luokan testauksessa on samat periatteet. Testit luovat statistics_test.csv tiedoston ja poistavat sen ennen assert-komentoja. Mikäli nimi on määritelty samaksi config.py tiedostossa, vaikuttaa testit tallennettuihin tietoihin. Tässä merkitys on keskeisempi, koska testien ajaminen pyyhkii pelitilastot.
