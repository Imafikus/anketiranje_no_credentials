import parser

#? Modul koji sluzi za proveru stvari koje je generisao parser.py

TITLE_EXAMPLE = "Neki title"
DESC_EXAMPLE = "Neki desc"

REQUIRED_TEXT_EXAMPLE = [{
    "type": "text",
    "title": "Neki tekst koji je obavezan",
    "helpText": "",
    "required": True
}]

NOT_REQUIRED_TEXT_EXAMPLE = [{
        "type": "text",
        "title": "Neki tekst koji je neobavezan",
        "helpText": "",
        "required": False
    }]

PADEZ_ACTIVITY_EXAMPLE = [
    {
        "type": "grid",
        "title": "padez1 \"Neki activity\"",
        "helpText": "",
        "required": True,
        "rows": ["Koliko je razumljivo", "Koliko je korisno", "Koliko je zanimljivo"],
        "columns": ["1", "2", "3", "4", "5"]
    },
    {
        "type": "text",
        "title": "Dodatan komentar o padez2 \"Neki activity\"",
        "helpText": "",
        "required": True
    }
]

PREDEFINED_ACTIVITY_EXAMPLE = [
    {
        "type": "grid",
        "title": "Predavanje \"Neki activity\"",
        "helpText": "",
        "required": True,
        "rows": ["Koliko je razumljivo", "Koliko je korisno", "Koliko je zanimljivo"],
        "columns": ["1", "2", "3", "4", "5"]
    },
    {
        "type": "text",
        "title": "Dodatan komentar o predavanju \"Neki activity\"",
        "helpText": "",
        "required": True
    }
]

SECTION_HEADER_EXAMPLE = [{
        "type": "sectionHeader",
        "title": "Neki section header",
        "helpText": ""
    }]

ACTIVITY_EXAMPLE = [
    {
        "type": "grid",
        "title": "Predavanje \"Neki activity\"",
        "helpText": "",
        "required": True,
        "rows": ["Koliko je razumljivo", "Koliko je korisno", "Koliko je zanimljivo"],
        "columns": ["1", "2", "3", "4", "5"]
    },
    {
        "type": "text",
        "title": "Dodatan komentar o predavanju \"Neki activity\"",
        "helpText": "",
        "required": True
    }
]

SCALE_EXAMPLE = [{
        "type": "scale",
        "title": "Neki scale",
        "helpText": "",
        "required": True,
        "boundLower": 1,
        "boundUpper": 5,
        "labelLower": "znacenje ocene1",
        "labelUpper": "znacenje ocene2"
    }]

def check():
    import pprint
    obr_title, obr_desc, obradjeni_podaci = parser.obradi_fajl("primer_forme.txt")

    test_data = (
        REQUIRED_TEXT_EXAMPLE +
        NOT_REQUIRED_TEXT_EXAMPLE +
        SECTION_HEADER_EXAMPLE + 
        PADEZ_ACTIVITY_EXAMPLE +
        PREDEFINED_ACTIVITY_EXAMPLE +        
        SCALE_EXAMPLE
    )
    
    assert test_data == obradjeni_podaci, "\n%s\n%s" % (str(test_data), str(obradjeni_podaci))
    assert TITLE_EXAMPLE == obr_title
    assert DESC_EXAMPLE == obr_desc

    pprint.pprint(obradjeni_podaci)
    
if __name__ == "__main__":
    check()