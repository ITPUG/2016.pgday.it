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
'EVENT_DATE': 'Tuesday, December 13',
'EVENT_LOCATION': 'Camera di Commercio, Prato',
'COPYRIGHT': '''© Copyright 2008-2016 Italian PostgreSQL Users Group<br>
VAT: 02099540979 / Tax Code: 92074760486
''',
'MENUITEMS': (('home', '/en'),),
'FOOTER_LINKS' : (
    ('Last edition', 'http://2015.pgday.it' ),
    ('volunteering', '/en/pages/volunteering.html' ),
),
'SCHEDULE': (
   ('09:00', [
        {
            'title': 'Registration'
        },
    ]),
    ('10:00', [
        {
            'track': 'auditorium',
            'title': 'Opening'
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
            'title': 'Break',
            'extra_class': 'schedule-item--generic-break',
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

)
## End of translated settings

    }
}

