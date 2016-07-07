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
EVENT_DATE = 'venerdi 25 novembre'
EVENT_LOCATION = 'camera di commercio, prato'
EVENT_LOCATION_COORDS = {
    'lat': '43.9322467',
    'lng': '10.9108973',
}
#MENUITEMS = (('home', ''),)
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
)
SCHEDULE = (
    ('08:30', [
        {
            'title': 'Registrazione'
        },
    ]),
    ('09:00', [
        {
            'track': 'auditorium',
            'title': 'Apertura Lavori'
        },
    ]),
    ('09:45', [
        {
            'track': 'auditorium',
            'title': 'Keynote',
            'speakers': [
                'Andres Freund',
            ]
        },
    ]),
    ('10:30', [
        {
            'title': 'Coffee Break',
            'extra_class': 'schedule-item--coffe',
        },
    ]),
    ('10:45', [
        {
            'track': 'auditorium',
            'title': 'BDR for DBAs',
            'speakers': [
                'Martin Marques',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Do you talk PostgreSQL?',
            'speakers': [
                'Denis Gasparin',
            ]
        },
    ]),
    ('11:30', [
        {
            'track': 'auditorium',
            'title': 'YeSQL: Battling the NoSQL Hype Cycle with Postgres',
            'speakers': [
                'Bruce Momjian',
            ],
            'level': 'hard',
            'language': 'english',
            'duration': '45 min',
        },
        {
            'track': 'sala conferenze',
            'title': 'PostgreSQL Disaster Recovery (con BarMan)',
            'speakers': [
                'Giulio Calacoci',
            ]
        },
    ]),
    ('13:00', [
        {
            'title': 'Pranzo',
            'extra_class': 'schedule-item--lunch',
        },
    ]),
    ('14:00', [
        {
            'track': 'auditorium',
            'title': 'Integrare PostgreSQL con Logstash per il monitoraggio real-time',
            'speakers': [
                'Gabriele Bartolini',
                'Marco Nenciarini',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'L\'importanza della profilazione delle query',
            'speakers': [
                'Gianni Ciolli',
            ]
        },
        {
            'track': 'sala informatica',
            'title': 'ITPUGLab',
            'speakers': [
                'Luca Ferrari',
                'Gianluca Riccardi',
            ],
            'duration': '120min',
            'level': 'easy',
            'language': 'italian',
        },
    ]),
    ('15:30', [
        {
            'title': 'Coffee Break',
            'extra_class': 'schedule-item--coffe',
        },
    ]),
    ('16:30', [
        {
            'track': 'auditorium',
            'title': 'Lightning Talk',
        },
    ]),
    ('17:30', [
        {
            'track': 'auditorium',
            'title': 'Foto di gruppo e chiusura dei lavori',
        },
    ]),
    ('18:00', [
        {
            'title': 'pg_beer',
            'extra_class': 'schedule-item--beer',
        },
    ]),
)

