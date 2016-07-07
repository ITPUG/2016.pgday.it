#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

I18N_SUBSITES = {
    'en': {

## Translated settings
'SITENAME': '2016 PGDay.IT',
'EVENT_CLAIM': '''We are working hard to organize the 10th
edition of PGDay.IT.<br>
Stay tuned to get news and follow the progress.
''',
'SITEURL': '/en',
'EVENT_DATE': 'Friday 25 November',
'EVENT_LOCATION': 'Chamber of Commerce, Prato',
'COPYRIGHT': '''© Copyright 2008-2016 Italian PostgreSQL Users Group<br>
VAT: 02099540979 / Tax Code: 92074760486
''',
'MENUITEMS': (('home', '/en'),),
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

