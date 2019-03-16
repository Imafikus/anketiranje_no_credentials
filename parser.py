import anketiranje

TITLE = "title"
DESC = "desc"
PADEZI = {
    "predavanje" : ("Predavanje", "predavanju"),
    "aktivnost" : ("Aktivnost", "aktivnosti")   
}

#? type samo sluzi da primi nepotreban parametar
#? ne koristimo to posle
def parse_title(red, _type, title):
    """
    Vadi title iz fajla koji opisuje anketu
    """

    if(red != 0):
        raise Exception("Title mora biti jedinstven i mora biti na pocetku!")

    print("parse_title")
    return title

def parse_description(red, _type, desc):
    """
    Vadi description za anketu iz fajla koji opisuje anketu
    """

    if(red != 1):
        raise Exception("Desc mora biti jedinstven i mora ici odmah posle title-a!")

    print("parse_description")
    return desc

def parse_text(text, title, required=False):
    """
    Vadi jedno text polje(objekat, kako god) iz fajla koji opisuje anketu
    """
    print("parse_text")

    parsed_data = [{
        "type": "text",
        "title": title,
        "helpText": "",
        "required": required
    }]
    
    return parsed_data    

def parse_section_header(section_header, title, required=False):
    """
    Vadi section_header iz fajla koji opisuje anketu
    """
    print("parse_section_header")

    parsed_data = [{
        "type": "sectionHeader",
        "title": title,
        "helpText": ""
    }]

    return parsed_data

def parse_activity(activity, title, padezi, required=False):
    """
    Pravi jednu akvivnost za anketu. Anketa se sastoji iz 3 pitanja
    i dodatnog textbox-a za komentar. Ta dva su odvojeni Google Form objekti
    i spajaju se u ovoj funkciji.
    """
    print("parse_activity")

    grid_title_part = ""
    text_title_part = ""

    #?proverava da li imamo predefinisane padeze
    if len(padezi.split()) == 1:
        if padezi.lower() in PADEZI:
            grid_title_part, text_title_part = PADEZI[padezi.lower()]
        else:
            raise Exception()
    
    #?eksplicitno zadat padez, budite pismeni
    else:
        grid_title_part = padezi.split()[0]
        text_title_part = padezi.split()[1]

    parsed_data = [
        {
            "type": "grid",
            "title": grid_title_part + " " + '"' + title + '"',
            "helpText": "",
            "required": required,
            "rows": ["Koliko je razumljivo", "Koliko je korisno", "Koliko je zanimljivo"],
            "columns": ["1", "2", "3", "4", "5"]
        },
        {
            "type": "text",
            "title": "Dodatan komentar o " + text_title_part + " " + '"' + title + '"',
            "helpText": "",
            "required": required
        }
    ]

    return parsed_data

def parse_scale(scale, title, strBoundLower, labelLower, strBoundUpper, labelUpper, required=False):
    """
    Vadi scale iz fajla koji opisuje anketu
    """

    print("parse_scale")

    boundLower = int(strBoundLower)
    boundUpper = int(strBoundUpper)

    parsed_data =  [{
        "type": "scale",
        "title": title,
        "helpText": "",
        "required": required,
        "boundLower": boundLower,
        "boundUpper": boundUpper,
        "labelLower": labelLower,
        "labelUpper": labelUpper
    }]

    return parsed_data

PARSERI = {
    "text": parse_text,
    "section_header": parse_section_header,
    "activity": parse_activity,
    "scale": parse_scale
}

def obradi_fajl(fajl):
    """
    Otvara fajl koji mu je prosledjen. Prolazi kroz fajl i vadi komponente.
    
    Ako neka komponenta nije dobro opisana vraca gresku i javlja na kojoj liniji u fajlu se 
    desila greska.

    """

    p_title = ""
    p_desc = ""
    lista_parsovanja = []

    with open(fajl, "r") as spisak_stvari: 
        try:
            for red, stvar in enumerate(spisak_stvari):
                komponente = list(map(lambda x: x.strip(), stvar.split(";")))

                vrsta_komponente = komponente[0].lower()

                isRequired = vrsta_komponente[-1] != '?'

                if not isRequired:
                    vrsta_komponente = vrsta_komponente[:-1] 

                if vrsta_komponente == "":
                    continue
                if(vrsta_komponente == TITLE): 
                    p_title = parse_title(red, *komponente)
                
                elif(vrsta_komponente == DESC): 
                    p_desc = parse_description(red, *komponente)

                elif vrsta_komponente in PARSERI: 
                    lista_parsovanja += PARSERI[vrsta_komponente](*komponente, required=isRequired)

                else:
                    raise Exception("Pogresan unos komponenti: " + str(komponente))
        
        except Exception as ex:
            print("Greska na liniji", red + 1, ":", ex)
            raise

    return p_title, p_desc, lista_parsovanja

def napravi_formu(fajl):
    """
    Prosledjuje fajl koji na obradu. Ono sto se vrati sa obrade sklapa
    u format koji podrzava GoogleAPI
    """
    
    title, desc, items = obradi_fajl(fajl)
    
    form_data = {
        "title" : title,
        "description" : desc,
        "items" : items
    }

    return form_data

if __name__ == "__main__":
    import argparse, sys

    parser_desc = """
        Prima putanju do fajla koji opisuje formu
    """
    parser = argparse.ArgumentParser(description=parser_desc)
    parser.add_argument('--noauth_local_webserver', help="Parametar koji se stavlja ako zabode ucitavanje", action = "store_true")
    parser.add_argument('file_path', type=str, help="Putanja do fajla koji opisuje formu")
    
    args = parser.parse_args()

    #? GoogleAPI se buni, a mi smo vec proverili argumente, pa sklanjamo da se on ne bi bunio
    del sys.argv[-1]

    forma = napravi_formu(args.file_path)

    #? Zove funkciju koja prica sa GoogleAPI-jem
    anketiranje.do_the_req(forma)
