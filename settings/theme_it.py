# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

##
# THEME CONFIG
##
SITENAME = 'PGDay.IT 2016'
BRANDING_LINK = {
    'href': 'http://www.itpug.org',
    'title': 'itpug',
    'image': 'logo-itpug.png',
}
EVENT_CLAIM = '''Stiamo lavorando per organizzare la decima
edizione del PGDay Italiano.<br>
Torna a trovarci per rimanere aggiornato con gli sviluppi!
'''
EVENT_DATE = 'martedì 13 dicembre'
EVENT_LOCATION = 'Camera di Commercio, Prato'
EVENT_LOCATION_COORDS = {
    'lat': '43.8727834',
    'lng': '11.0950403',
}
MENUITEMS = (('home', ''),)
'''
EVENT_CTA_BUTTONS = [
    {
        'label': 'biglietti conferenza',
        'url': 'https://www.eventbrite.it/',
        'primary': True
    },
    {
        'label': 'biglietti cena',
        'url': 'https://www.eventbrite.it/',
        'primary': False
    },
]
'''
COPYRIGHT = '''© Copyright 2008-2016 Italian PostgreSQL Users Group<br>
Partita IVA: 02099540979 / Codice Fiscale: 92074760486
'''
'''
SOCIAL_EVENTS = [
    {
        'title': 'pg_birra',
        'when': 'giovedi 16, ore 18:00',
        'where': 'Camelot 3.0',
        'map': 'https://www.google.it/maps',
        'description': 'Una birra gentilmente offerta da carlo',
    }, {
        'title': 'pg_birra',
        'when': 'venerdi 17, ore 18:00',
        'where': 'Camelot 3.0',
        'map': 'https://www.google.it/maps',
        'description': 'Per bere in compagnia e parlare anche di Postgres',
    }, {
        'title': 'pg_cena',
        'when': 'venerdi 17 - 20:00',
        'where': 'Pizzeria da Peppino',
        'map': 'https://www.google.it/maps',
        'description': 'Un menu\' per sfamare tutte le bocche, e si parla di Postgres',
    }
]
'''
'''
EVENT_PARTNERS = {
    'diamond': [{
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }, {
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }, {
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }],
    'platinum': [{
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }],
    'gold': [{
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }, {
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }],
    'silver': [],
    'media': [{
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }, {
        'name': 'Amiga',
        'url': 'http://www.amiga.org/',
        'logo': 'logo-sponsor.png',
    }],
}
'''
SOCIAL_LINKS = [
    {
        'name': 'facebook',
        'url': 'https://www.facebook.com/PGDay.IT/',
        'icon': 'facebook',
        'hide_name': True,
    }, {
        'name': 'twitter',
        'url': 'https://twitter.com/PGDayIT',
        'icon': 'twitter',
        'hide_name': True,
    }, {
        'name': 'google plus',
        'url': 'https://plus.google.com/114060631874544975126',
        'icon': 'google-plus',
        'hide_name': True,
    },
]
FOOTER_LINKS = (
    ('passata edizione', 'http://2015.pgday.it' ),
    ('aiutaci', '/pages/volunteering.html' ),
)
SCHEDULE = (
    ('09:00', [
        {
            'title': 'Registrazione'
        },
    ]),
    ('10:00', [
        {
            'track': 'auditorium',
            'title': 'Apertura Lavori'
        },
    ]),
    ('10:15', [
        {
            'track': 'auditorium',
            'title': 'Keynote',
            'speakers': [
                'TBA',
            ]
        },
    ]),
    ('11:00', [
        {
            'title': 'Coffee Break',
            'extra_class': 'schedule-item--coffe',
        },
    ]),
    ('11:25', [
        {
            'track': 'auditorium',
            'title': 'Don\'t Touch that Parameter',
            'speakers': [
                'Mladen Marinovic',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Estensione del supporto BRIN a PostGIS',
            'speakers': [
                'Giuseppe Broccolo',
            ]
        },
    ]),
    ('12:10', [
        {
            'title': 'Pausa',
            'extra_class': 'schedule-item--coffe',
        },
    ]),
    ('12:20', [
        {
            'track': 'auditorium',
            'title': 'Upgrade or not upgrade... this is the question!',
            'speakers': [
                'Denis Gasparin',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'PostgreSQL - Hadoop: why not?',
            'speakers': [
                'Matteo Durighetto',
            ]
        },
    ]),
    ('13:05', [
        {
            'title': 'Pranzo',
            'extra_class': 'schedule-item--lunch',
        },
    ]),
    ('14:05', [
        {
            'track': 'auditorium',
            'title': 'ITPUG - Italian PostgreSQL Users Group',
            'speakers': [
                'Consiglio Direttivo ITPUG',
            ]
        },
    ]),
    ('14:20', [
        {
            'track': 'auditorium',
            'title': 'PostgreSQL su NFS: miti e verità',
            'speakers': [
                'Jonathan Battiato',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Postgrest: la REST API per i database PostgreSQL',
            'speakers': [
                'Lucio Grenzi',
            ]
        },
        {
            'track': 'sala informatica',
            'title': 'ITPUGLab',
            'speakers': [
                'Luca Ferrari',
                'Gianluca Riccardi',
            ],
            'duration': '115min',
        },
    ]),
    ('15:05', [
        {
            'title': 'Coffee Break',
            'extra_class': 'schedule-item--coffe',
        },
    ]),
    ('15:30', [
        {
            'track': 'auditorium',
            'title': 'PostgreSQL Horror Stories Vol.1: Failing on the big day',
            'speakers': [
                'Mladen Marinovic',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Unit Test',
            'speakers': [
                'Andrea Adami',
            ]
        },
    ]),
    ('16:15', [
        {
            'track': 'auditorium',
            'title': 'Lightning Talk',
        },
    ]),
    ('17:15', [
        {
            'track': 'auditorium',
            'title': 'Foto di gruppo e chiusura dei lavori',
        },
    ]),
    ('17:45', [
        {
            'title': 'pg_beer',
            'extra_class': 'schedule-item--beer',
        },
    ]),
)

