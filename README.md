# Automatsko generisanje Google Forms ankete 

Ovaj program generiše Google Forms ankete na osnovu fajla koji opisuje traženu anketu.

Ideja ovog programa je da smanji vreme koje je potrebno da se izgeneriše anketa koja se daje na kraju svakog seminara matematičko-tehničkih nauka (TEH) u IS Petnica.

## Korišćenje

Za korišćenje programa je potrebno da napravite poseban fajl u kome ćete opisati vašu anketu.  
Svaki objekat koji napravite mora poštovati tačno određenu sintaksu i **mora biti u posebnom redu**

Fajl teh2019zimski je primer definisane forme, pa se tu može videti kako mora da izgleda obeležavanje

Sintaksa se sastoji od ključnih reči odvojenih sa ' ; '

U nastavku su dati detaljni opisi svih (za sada) podržanih elemenata



### Title

Title predstavlja naslov forme, mora biti zadat na početku vašeg fajla. Izgleda ovako:

`title; Neki title `

### Description

Description je deo koju **uvek ide posle title dela**. Izgleda ovako:

`desc; Neki desc`

### Obavezne i neobavezne stvari

Kod svih stvari koje treba da se popune na neki način postoji opcija da budu obavezne / neobavezne za popunjavanje.  
**Stvari koje želite da vam budu neobavezne označavate sa sufiksom ? koji se nalepi na kraj pojma**

### Text

Text deo se sastoji od pitanja i textboxa u koji treba da se upiše odgovor na pitanje. Mogu biti obavezni i neobavezni:

`text; Neki tekst koji je obavezan`  

`text?; Neki tekst koji je neobavezan`

### Section Header

Section Header služi da odvoji sekcije ankete. Izgleda ovako:

`section_header; Neki section header`

### Activity
Activity predstavlja veći deo forme i **sastoji se iz par pitanja na koje odgovori treba da se daju u vidu ocene, i sastoji se iz dodatnog komentara koji treba da se da.**  

Bitna stvar koja treba da se primeti kod predavanja je što srpski jezik ima padeže, pa je nezgodno kada treba da opišemo **predavanje** i damo dodatan komentar o **predavanju**.  
Kako je gomila stvari koja se dešava uglavnom predavanje ili aktivnost, ova dva su predefinisana i dovoljno je napisati samo jednu reč, ako ne koristimo ova 2, moramo da napišemo naše promene po padežima. Razni primeri ispod:

`activity; Neko predavanje; predavanje` - Ovo će izgenerisati rečenice:
- Predavanje "Neko predavanje"
- Dodatan komentar o predavanju "Neko predavanje"

`activity; Neka igra; Igra igri` - Ovo će izgenerisati rečenice:
- Igra "Neka igra"
- Dodatan komentar o igri "Neka igra"

I ovde se znakom ? označava da li se ovo polje ne mora popunjavati.

### Scale

Scale je element koji označava skalu i služi da polaznici u vidu ocene daju odgovor o nekom pitanju. Izgleda ovako:

`scale; Neki scale; 1; znacenje ocene1; 5; znacenje ocene2`

Ocene moraju biti celi brojevi. Redosled kojim se moraju unositi stvari odgovara primeru koji je dat.

Kao i sve ostalo, i ovde se znakom ? označava da li se ovo polje ne mora popunjavati.

## Korišćenje same skripte


**VAŽNO:** Projektu fali *credentials.json* fajl koji je namerno izostavljen jer sadrži informacije koje ne bi trebalo da se drže u public folderu. Fajl možete naći u folderu na drajvu i samo je potrebno da ga prekopirate ovde.


Skripta se poziva tako što ukucate:   
`python3 parser.py putanja_do_opisa_ankete`

Kako se GoogleAPI (očigledno) povezuje sa Google nalogom, prilikom prvog pokretanja će vam iskočiti u pretraživaču opcija da se prijavite na neki Google nalog.  
Ako ovo iz bilo kog razloga ostane u beskonačnom učitavanju skriptu treba da zovete sa komandom:

`python3 parser.py --noauth_local_webserver putanja_do_opisa_ankete`

## Korišćenje pipenv

Svi dependency-ji koji se koriste se nalaze u *Pipfile* fajlu.

Program može da se koristi tako što ćete napraviti poseban pipenv za vaš fajl koji dobijate kada ukucate:

`pipenv shell`

Ako nemate pipenv, instalirate ga sa:

`pip install --user pipenv`

Ako ne želite da koristite pipenv, treba samo da imate sve pakete koji se zahtevaju
