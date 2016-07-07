#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

I18N_SUBSITES = {
    'en': {

## Translated settings
'SITENAME': '2016 PGDay.IT',
'EVENT_CLAIM': '''ITPUG is pleased to present the ninth edition of PGDay.IT.
You will find talks about PostgreSQL, a team of volunteers ready to help you
if necessary, social events and much more...
''',
'SITEURL': '/en',
'EVENT_DATE': 'Friday 23 October',
'EVENT_LOCATION': 'Chamber of Commerce, Prato',
'EVENT_CTA_BUTTONS': [
    {
        'label': 'conference tickets',
        'url': 'https://www.eventbrite.it/',
        'primary': True
    },
    {
        'label': 'dinner tickets',
        'url': 'https://www.eventbrite.it/',
        'primary': False
    },
],
'COPYRIGHT': '''© Copyright 2008-2016 Italian PostgreSQL Users Group<br>
VAT: 02099540979 / Tax Code: 92074760486
''',
'SOCIAL_EVENTS': [
    {
        'title': 'pg_beer',
        'when': 'Thursday 16, 18:00',
        'where': 'Camelot 3.0',
        'map': 'https://www.google.it/maps',
        'description': 'A beer kindly offered by carlo',
    }, {
        'title': 'pg_beer',
        'when': 'Friday 17, 18:00',
        'where': 'Camelot 3.0',
        'map': 'https://www.google.it/maps',
        'description': 'To drink all together and talk about Postgres',
    }, {
        'title': 'pg_dinner',
        'when': 'Friday 17 - 20:00',
        'where': 'Pizzeria da Peppino',
        'map': 'https://www.google.it/maps',
        'description': 'A menu to feed al mouths, and we talk about Postgres',
    }
],
'FOOTER_LINKS' : (
    ('Last edition', 'http://2015.pgday.it' ),
),
'SCHEDULE': (
    ('08:30', [
        {
            'title': 'Registration'
        },
    ]),
    ('09:00', [
        {
            'track': 'auditorium',
            'title': 'Conference opening'
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
            'track': 'conference hall',
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
            ]
        },
        {
            'track': 'conference hall',
            'title': 'PostgreSQL Disaster Recovery (using BarMan)',
            'speakers': [
                'Giulio Calacoci',
            ]
        },
    ]),
    ('13:00', [
        {
            'title': 'Lunch',
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
            'track': 'conference hall',
            'title': 'The importance of query profiling',
            'speakers': [
                'Gianni Ciolli',
            ]
        },
        {
            'track': 'computer science room',
            'title': 'ITPUGLab',
            'speakers': [
                'Luca Ferrari',
                'Gianluca Riccardi',
            ]
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
            'title': 'Lightning Talks',
        },
    ]),
    ('17:30', [
        {
            'track': 'auditorium',
            'title': 'Group photo and conference ending',
        },
    ]),
    ('18:00', [
        {
            'title': 'pg_beer',
            'extra_class': 'schedule-item--beer',
        },
    ]),
)
## End of translated settings

    }
}

