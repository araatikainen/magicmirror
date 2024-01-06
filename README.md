# Magic mirror


Magic Mirror projekti on peilin ja infonäytön risteytys. Peili on suunniteltu käyttäen SolidWorks ohjelmaa ja 3d tulostettu. Infonäyttönä toimii vanhan läppärin 13" näyttö, joka on irroitettu ja yhdistetty raspiin käyttäen lcd controlleria. Toteutus infonäytölle löytyy "mirror" kansiosta.


## Peili

Peilin kehykset suunniteltu SolidWorksillä näytön koon mukaan. 3d-printattu kahdessa osassa tulostimen rajoitusten takia.

| Kuva 1                                              | Kuva 2                                              |
|------------------------------------------------------|------------------------------------------------------|
| ![Kehys 1](https://github.com/araatikainen/magicmirror/assets/107348864/83f7ab36-1978-450e-af72-b5ebea3708b1) | ![Kehys 2](https://github.com/araatikainen/magicmirror/assets/107348864/5326cc4b-71ee-4ff7-abb8-d5f360541e44) |


Peililevy tilattu netistä ja sen tulee olla yksisuuntainen. Tällöin valo pääsee peilin läpi kulkemaan ja saadaan käyttäjälle näkymään peilikuva ja infonäytön tiedot samaan aikaan.
Näyttö on yhdistetty lcd controllerin kautta raspiin. Lcd controllerissa tärkeää oli katsoa sen olevan sopiva näytölle.


## Infonäyttö

Flask-sovellus, joka hyödyntää useita reittejä palvelemaan eri tarkoituksia. Se tarjoaa ajankohtaista tietoa ajasta, lauseita, ruokalistaa, säätietoja ja Nysse-julkisen liikenteen aikatauluja. 
Sovellus hakee ajankohtaiset tiedot käyttäen api kutsuja.\
&nbsp;\
Ruokalistat -- unisafka.fi\
Säätiedot -- ilmatieteenlaitos.fi\
Nysse -- api.digitransit.fi\
&nbsp;

Näytön värimaailmassa on käytetty tummia taustavärejä näytön tekstien erottuvuuden vuoksi. Lisäksi peilautuvuutta voi säädellä helposti vaihtelemalla näytönkirkkautta ja taustavalon määrää.
