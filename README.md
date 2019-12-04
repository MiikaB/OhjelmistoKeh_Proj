# Ohjelmistokehitys Projekti

## Projektini on Python Scripti SSH-Tunnelin luomiseen Tietokone-Koulu välillä

Tavoite on käynnistää scripti ja koordinoida nro (1-3) ohjelmassa, päättäen käynnistetäänkö tunneli, suljetaanko se, ja lopeta scripti

Idea projektiin tuli oikeasta tarpeesta luoda tunneli, jotta pääsen käsiksi koulun luomaan mysql tietokantaan

Ennen projektia jouduin avaamaan putty tunnelin manuaalisesti ja lisäksi kirjautumaan ssh-yhteyden muodostamiseksi

Nyt scriptin valmistuttua tunnelin luomisessa kestää noin 3 sekunttia!

Vaikeus asteella scriptiin meni aktiiviset ~6h pähkaillen eri python moduuleita. Lopulta scripti lähti toimimaan vankan kokeilemisen kautta ja opetti, kuinka pythonilla voi suorittaa myös muita terminaalikutsuja, sekä avata ohjelmia.

## Ngrok

Implimentoin scriptiin python moduulin Ngrok, joka luo sertifikaatin paikalliselle yhteydelle (localhost). Samalla kun scripti kirjautuu mariaDB tietokantaan, antaa se komennon käynnistää Ngrok määritetyllä portilla ja printtaa käynnistynyt https-yhteys konsoliin. Ngrok on erittäin hyödyllinen lisäys, sillä ilman https-yhteyttä erillistä paikallista back-endiä ei pysty lukemaan get-pyynnöllä (Get-pyyntö onnistuu, mutta data ei kulje toisin kuin https yhteydellä Get-pyyntö onnistuu ja data kulkee ja näkyy)

## !HUOM

Scriptiin pitää lisätä käyttäjätunnus sekä salasana ssh-yhteyden muodostamiseksi, ja turvallisuus syistä olen jättänyt ne githubista pois.
