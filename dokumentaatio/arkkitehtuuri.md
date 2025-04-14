# Arkkitehtuurikuvaus

## Rakenne

Luokka/pakkauskaavio:

![Luokka/pakkauskaavio](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Päätoiminnallisuudet

### Uuden käyttäjän luominen

Käyttäjä luo uuden käyttäjätunnuksen ja salasanan kirjoittamalla ne annettuihin kenttiin ja sen jälkeen klikkaamalla "Create"-nappia. Napin painaminen kutsuu GameServicen create_user -metodia parametreilla uusi käyttäjätunnus ja uusi salasana. Sovellus tarkistaa ensin UserRepositoryn find_by_username -metodilla, että käyttäjää ei ole vielä olemassa ja luo sitten uuden käyttäjän create-metodilla. Tämän jälkeen käyttöliittymän näkymä vaihtuu create_user_view-näkymästä game_view-näkymään.

![Uuden käyttäjän luonti](./kuvat/kayttajanluomis-sekvenssi.png)

### Kirjautuminen

Käyttäjä kirjautuu kirjoittamalla olemassa olevan käyttäjätunnuksen ja salasanan olemassa oleviin kenttiin ja sen jälkeen klikkaamalla "Login"-nappia. Napin painaminen kutsuu Game Servicen login-metodia parametreilla käyttäjätunnus ja salasana. Sovellus tarkistaa ensin UserRepositoryn find_by_username -metodilla, että käyttäjä on olemassa ja sitten, että salasana täsmää. Tämän jälkeen käyttöliittymän näkymä vaihtuu login-näkymästä game_view-näkymään.

![Kirjautuminen](./kuvat/kirjautumis-sekvenssi.png)

### Pelin aloittaminen

Peli aloitetaan painamalla "Start Game"-nappia. Napin painaminen kutsuu GameServicen start-metodia, joka puolestaan kutsuu parametreilla board ja cell_size Game-luokkaa. Pelin alkuvalmistelut tehdään Gamen add_new_ships ja initialize_sprites -metodeilla, jonka jälkeen GameService käynnistää pygame-ikkunan.
