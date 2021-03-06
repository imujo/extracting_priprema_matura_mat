import json

pages = [
    {
        "cjelina": "Brojevi i algebra",
        "lekcija": "Skupovi brojeva",
        'podlekcija': 'Skupovi prorodnih, cijelih, racionalnih i realnih brojeva',
        'zadatci': (24, 30),
        'rjesenja': (29, 31)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Potencije',
        'zadatci': (35, 39),
        'rjesenja': (38, 39)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Korjeni',
        'zadatci': (42, 46),
        'rjesenja': (45, 46)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Kamatni račun',
        'zadatci': (57, 63),
        'rjesenja': (62, 64)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Uređaj u skupu realnih brojeva',
        'zadatci': (67, 69),
        'rjesenja': (68, 69)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Mjerne jedinice',
        'zadatci': (72, 74),
        'rjesenja': (73, 74)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Apsolutna vrijednost',
        'zadatci': (76, 78),
        'rjesenja': (77, 78)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Skupovi brojeva',
        'podlekcija': 'Kompleksni brojevi',
        'zadatci': (85, 89),
        'rjesenja': (88, 90)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Algebarski izrazi i razlomci',
        'podlekcija': 'Algebarski razlomci',
        'zadatci': (94, 97),
        'rjesenja': (97, 98)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Algebarski izrazi i razlomci',
        'podlekcija': 'Algebarski razlomci',
        'zadatci': (100, 104),
        'rjesenja': (103, 104)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Algebarski izrazi i razlomci',
        'podlekcija': 'Binomni poučak',
        'zadatci': (108, 111),
        'rjesenja': (110, 111)
    },
    {
        'cjelina': 'Brojevi i algebra',
        'lekcija': 'Algebarski izrazi i razlomci',
        'podlekcija': 'Polinomi',
        'zadatci': (114, 116),
        'rjesenja': (116, 117)
    },
    #     # -------------------
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Pojam funkcije',
        'podlekcija': 'Pojam funkcije',
        'zadatci': (125, 131),
        'rjesenja': (131, 133)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Linearna funkcija',
        'podlekcija': 'Linearna funkcija',
        'zadatci': (142, 147),
        'rjesenja': (147, 149)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Linearna funkcija',
        'podlekcija': 'Linearna jednadžba',
        'zadatci': (152, 154),
        'rjesenja': ()
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Linearna funkcija',
        'podlekcija': 'Sustavi linearnih jednadžbi',
        'zadatci': (157, 159),
        'rjesenja': ()
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Linearna funkcija',
        'podlekcija': 'Linearna jednadžba - zadatci',
        'zadatci': (161, 166),
        'rjesenja': (165, 167)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Linearna funkcija',
        'podlekcija': 'Linearna nejednadžba',
        'zadatci': (171, 174),
        'rjesenja': (173, 174)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Funkcija apsolutne vrijednosti',
        'podlekcija': 'Funkcija apsolutne vrijednosti',
        'zadatci': (178, 182),
        'rjesenja': (181, 185)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Funkcija apsolutne vrijednosti',
        'podlekcija': 'Jednadžbe i nejednadžbe s apsolutnim vrijednostima',
        'zadatci': (189, 191),
        'rjesenja': (190, 191)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Kvadratna funkcija',
        'podlekcija': 'Kvadratna funkcija',
        'zadatci': (204, 210),
        'rjesenja': (209, 215)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Kvadratna funkcija',
        'podlekcija': 'Kvadratna jednadžba',
        'zadatci': (220, 224),
        'rjesenja': (224, 225)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Kvadratna funkcija',
        'podlekcija': 'Kvadratna nejednadžba',
        'zadatci': (229, 231),
        'rjesenja': (231, 232)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Kvadratna funkcija',
        'podlekcija': 'Funkacija drugog korjena',
        'zadatci': (235, 237),
        'rjesenja': (237, 239)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Kvadratna funkcija',
        'podlekcija': 'Iracionalna jednadžba i nejednadžba',
        'zadatci': (241, 243),
        'rjesenja': (243, 244)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Eksponencionalna funkcija',
        'zadatci': (249, 253),
        'rjesenja': (253, 257)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Logaritamska funkcija',
        'zadatci': (263, 268),
        'rjesenja': (267, 270)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Eksponencijalna jednadžba',
        'zadatci': (272, 274),
        'rjesenja': (274, 275)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Logaritamska jednadžba',
        'zadatci': (280, 283),
        'rjesenja': (282, 283)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Eksponencijalna nejednadžba',
        'zadatci': (284, 286),
        'rjesenja': (286, 287)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Eksponencionalna i logaritamska funkcija',
        'podlekcija': 'Logaritamska nejednadžba',
        'zadatci': (289, 291),
        'rjesenja': (291, 292)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Trigonometrijske funkcije',
        'podlekcija': 'Trigonometrijske funkcije',
        'zadatci': (314, 321),
        'rjesenja': (320, 326)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Trigonometrijske funkcije',
        'podlekcija': 'Trigonometrijski identiteti',
        'zadatci': (331, 334),
        'rjesenja': (333, 334)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Trigonometrijske funkcije',
        'podlekcija': 'Trigonometrijske jednadžbe',
        'zadatci': (344, 348),
        'rjesenja': (347, 348)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Trigonometrijske funkcije',
        'podlekcija': 'Trigonometrijske nejednadžbe',
        'zadatci': (350, 352),
        'rjesenja': (351, 352)
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Domena i slaganje funkcija',
        'podlekcija': 'Domena funkcije',
        'zadatci': (354, 358),
        'rjesenja': ()
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Domena i slaganje funkcija',
        'podlekcija': 'Slaganje funkcija',
        'zadatci': (359, 360),
        'rjesenja': ()
    },
    {
        'cjelina': 'Funkcije, jednadžbe i nejednadžbe',
        'lekcija': 'Inverzne funkcije',
        'podlekcija': 'Inverzne funkcije',
        'zadatci': (365, 373),
        'rjesenja': (372, 378)
    },
    #     # -------------------
    {
        'cjelina': 'Nizovi',
        'lekcija': 'Aritmetiči i geometrijski nizovi',
        'podlekcija': 'Zadatci',
        'zadatci': (388, 395),
        'rjesenja': (394, 395)
    },
    #     # --------------------
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Elementarna geometrija likova u ravnini',
        'podlekcija': 'Trokut',
        'zadatci': (407, 417),
        'rjesenja': (417, 418)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Elementarna geometrija likova u ravnini',
        'podlekcija': 'Četverokut i mnogokut',
        'zadatci': (425, 432),
        'rjesenja': (431, 433)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Elementarna geometrija likova u ravnini',
        'podlekcija': 'Krug i kružnica',
        'zadatci': (436, 441),
        'rjesenja': (440, 441)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrija prostora',
        'podlekcija': 'Zadatci',
        'zadatci': (444, 449),
        'rjesenja': (449, 451)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Prizma',
        'zadatci': (454, 460),
        'rjesenja': (460, 461)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Piramida',
        'zadatci': (465, 468),
        'rjesenja': (488, 369)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Valjak',
        'zadatci': (470, 474),
        'rjesenja': (473, 474)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Stožac',
        'zadatci': (476, 479),
        'rjesenja': (478, 479)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Kugla',
        'zadatci': (481, 484),
        'rjesenja': (483, 484)
    },
    {
        'cjelina': 'Geometrija',
        'lekcija': 'Geometrijska tijela',
        'podlekcija': 'Rotacijska tijela',
        'zadatci': (485, 487),
        'rjesenja': (486, 487)
    },
    #     # --------------------
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Koordinatni sustav na pravcu i u ravnini',
        'podlekcija': 'Udaljenost točaka na brojevnom pravcu',
        'zadatci': (494, 498),
        'rjesenja': (497, 499)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Vektori',
        'podlekcija': 'Zadatci',
        'zadatci': (506, 509),
        'rjesenja': (509, 510)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Pravac',
        'podlekcija': 'Zadatci',
        'zadatci': (518, 525),
        'rjesenja': (525, 528)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Krivulje drugog reda',
        'podlekcija': 'Kružnica',
        'zadatci': (535, 539),
        'rjesenja': (539, 540)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Krivulje drugog reda',
        'podlekcija': 'Elipsa',
        'zadatci': (546, 549),
        'rjesenja': (549, 550)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Krivulje drugog reda',
        'podlekcija': 'Hiperbola',
        'zadatci': (554, 556),
        'rjesenja': (556, 557)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Krivulje drugog reda',
        'podlekcija': 'Parabola',
        'zadatci': (559, 561),
        'rjesenja': (560, 561)
    },
    {
        'cjelina': 'Analitička geometrija',
        'lekcija': 'Krivulje drugog reda',
        'podlekcija': 'dodatak',
        'zadatci': (563, 565),
        'rjesenja': (564, 565)
    },
    #     # --------------------
    {
        'cjelina': 'Derivacije',
        'lekcija': 'Derivacije funkcija',
        'podlekcija': 'Zadatci',
        'zadatci': (572, 576),
        'rjesenja': (575, 576)
    },
    {
        'cjelina': 'Derivacije',
        'lekcija': 'Primjena derivacija',
        'podlekcija': 'Zadatci 1',
        'zadatci': (580, 581),
        'rjesenja': ()
    },
    {
        'cjelina': 'Derivacije',
        'lekcija': 'Primjena derivacija',
        'podlekcija': 'Zadatci 2',
        'zadatci': (594, 602),
        'rjesenja': (601, 605)
    },
]


with open('book.json', 'w') as json_file:
    json.dump(pages, json_file)
