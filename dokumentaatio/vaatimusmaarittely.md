## Sovellus
Miinaharava. Pelin tarkoitus on klikata ruutuja, jotka paljastavat kuinka monta miinaa on viereisissä ruuduissa. Tarkoitus olla klikkaamatta miinoja ja selvitää kaikkien miinojen sijainti, jolloin voittaa pelin. Jos klikkaa miinaa häviää pelin. 
## Käyttöliittymä
Alustavasti paljon inspiraation alkuperäisestä versiosta. 

Peliruudukko, jossa peliä pelataan.

Endgame ikkuna, joka ilmoittaa voititko vai hävisitkö pelin ja statistiikan liittyen juuri pelattun pelin kokoon. Esimerkiksi jos pelaat 10x10 ruudukon, jossa on 10 miinaa, peli näyttää siihen liittyviä tietoja. Ikkunassa on painikkeet uudelle pelille ja sovelluksen lopetukselle.

Asetusikkuna, jossa voi vaihtaa ruudukon kokoa ja miinojen määrää. 

Statistiikkaikkuna, josta voit valita ruudukon koon ja nähdä siihen liittyvät statistiikat. Painikkeet statistiikan resetoinnille.

<img src="https://github.com/ElomaaTapio/ot-harjoitustyo/blob/main/dokumentaatio/kuvat/Scan.jpg">
## Toiminnallisuudet
 - [X] Toimiva peli. Ruutujen arvot, miinat, klikkailu. 
 - [X] Kello.
 - [x] Mahdollisuus liputtaa ruutuja osoittamaan miinaa ja miinalaskuri.
 - [x] Eri kokoiset ruudukot ja settings ikkuna, josta ruudukkon kokoa voi vaihtaa.
 - [X] Ruutujen tuplaklikkaus ominaisuus. Jos ruudun ympäriltä on jo liputettu sen arvon verran miinoja, peli klikkaa automaattisesti kaikki ruudun vieressä olevat ruudut auki.
 - [x] Perusteema. 
 - [X] Game Over ikkuna.
 - [X] Statistiikka + ikkuna.
 - [X] Ensimmäinen avaus on aina 0.
 #### Kehitysideoita
 - [ ] Statistiikan laajennus. Käyttäjät. Useammat highscoret.
 - [ ] Toiston poisto Settings ja Statistics luokista. Jokaisessa UI luokassa on myös toistettuna pelin asetusten hakeminen.
 - [ ] Logiikan eriyttäminen vielä enemmän GameUI luokasta. Esim game-over konditiot. 
 - [ ] Animaatiot ja lisäteemat.
 - [ ] Musiikki?
