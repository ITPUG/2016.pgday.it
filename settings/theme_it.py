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
    'lat': '43.872372',
    'lng': '11.097499',
}
MENUITEMS = (('home', ''),)
EVENT_CTA_BUTTONS = [
    {
        'label': 'biglietti conferenza',
        'url': 'https://pgdayit2016.eventbrite.it/',
        'primary': True
    },
]
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
            'abstract': '''When you first start using PostgreSQL you use it with the default parameters and you are confident that they are chosen to provide a conservative but stable experience. As your knowledge of the database expands you start reading the documentation more and more and then the time comes to tweak the parameters by yourself. The documentation clearly states that some parameters are more dangerous than others, eg. fsync = off, but there are plenty more parameters that, in the right circumstances, can cause the database to misbehave, to become very slow, or to just stop working and fail.<br><br>

This presentation will present a handful of parameters and theoretical (or better yet absurd) situations in which the specific values chosen can cause problems. Some of the problems are interesting, some annoying and some are just unbelievable.<br><br>

If time will allow, the most interesting situations will be demonstrated on a running instance of PostgreSQL.
            ''',
            'speakers': [
                'Mladen Marinovic',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Estensione del supporto BRIN a PostGIS',
            'abstract': '''È sempre più comune oggi avere a che fare con basi di dati che raggiungono diversi terabyte, ed anche l'ambito geospaziale non fa eccezione. PostGIS, l'estensione geospaziale di PostgreSQL, si basa sull'indicizzazione GiST, mostrando notevoli prestazioni in presenza di grosse moli di dati. Ma man mano che le dimensioni di un dataset aumentano, le prestazioni degradano, fino a rendere l'indice non utilizzabile quando iniziano ad essere di dimensioni tali da non essere più contenuti in RAM.<br><br>

Il supporto BRIN, introdotto in PostgreSQL 9.5, permette di usare una indicizzazione tale da mantenere alte prestazioni anche per grosse basi di dati, fino all'ordine dei petabyte.<br><br>

In questo talk voglio presentare la patch che permette di estendere il supporto BRIN ai tipi di dato geospaziali inclusi in PostGIS, a cui ho personalmente contribuito ed introdotta nel recente rilascio della versione 2.3.0. Con l'occasione verranno presentati alcuni benchmark su dataset reali che permettono di mostrare i punti di forza (ma anche quelli deboli) di questo tipo di indicizzazione in ambito geospaziale.
            ''',
            'speakers': [
                'Giuseppe Broccolo',
            ]
        },
    ]),
    ('12:10', [
        {
            'title': 'Pausa',
            'extra_class': 'schedule-item--generic-break',
        },
    ]),
    ('12:20', [
        {
            'track': 'auditorium',
            'title': 'Upgrade or not upgrade... this is the question!',
            'abstract': '''Spesso e volentieri sistemisti ed amministratori di sistema si scontrano con gli sviluppatori per avere l'ultima release di PostgreSQL:<br><br>
- gli sviluppatori richiedono l'ultima release per avere accesso ad una particolare feature non disponibile nelle versioni precedenti<br>
- gli amministratori di sistema sono invece più conservativi perché la migrazione richiede un'attività sistemistica importante nonché un downtime non sempre trascurabile.<br><br>
L'obiettivo principale del talk è illustrare ai partecipanti le modalità di aggiornamento da 9.4 a 9.5/9.6 di PostgreSQL.
In particolare verranno illustrate le due modalità principali:<br>
- pg_upgrade<br>
- pg_logical<br><br>
Verrà presentato un tool (pg_repup, non ancora rilasciato pubblicamente) che sto scrivendo ed il cui sorgente sarà disponibile su github che semplifica e consente di aggiornare da una major release di PostgreSQL ad un'altra riducendo al minimo il downtime.
Il tool si propone di fatto come interfaccia semplificata di pg_logical.
            ''',
            'speakers': [
                'Denis Gasparin',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'PostgreSQL - Hadoop: why not?',
            'abstract': '''Tipicamente negli RDBMS tradizionali usati come DWH,
prima o poi abbiamo problematiche di offloading o
di utilizzare nuove tipologie di analisi che richiedono
un sistema multinodo, magari incrociando varie tipologie di dato,
sfrutto Spark o tecnologie similari.<br><br>

PostgreSQL ha compiuto notevoli passi avanti con l'introduzione
del hot standby e di alcune sue versioni  multimaster/ scalabili
( postgresql xl / bdr / postgres xc etc  ), tuttavia
per determinate tipologie di workload e analisi è utile spesso eseguire offloading del dato da PostgreSQL ad Hadoop e permettere
 lo scambio di dati tra i due sistemi.
Nel talk si illustreranno :<br>
*) architettura<br>
*) casi d'uso dell'offloading / integration<br>
*) metodologie di porting del dato da PostgreSQL ad Hadoop<br>
*) fdw per rendere trasparente l'estensione della base dati postgres con quella Hadoop<br>
*) hue -> postgresql  e presto -> postgresql
            ''',
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
            'abstract': '''Abbiamo avuto l'occasione di lavorare alla richiesta di un cliente, di
valutare in maniera obiettiva la possibilità di basare un database
PostgreSQL su Network File System.
Sono stati scritti molti articoli a riguardo, ma quando si ha
l'opportunità di mettere in pratica questa configurazione in prima
persona, ci si rende conto che ancora molto non è stato documentato.
Le prestazioni di NFS possono essere molto buone, ma si abbassano
notevolmente quando si inseriscono vincoli di affidabilità.
Una soluzione può essere quella di basare PostreSQL su 2 partizioni NFS,
una per i dati e una per gli xlog, in modo distinguere una
configurazione per un rapido accesso ai dati e una con maggiore
affidabilità per le scritture consistenti dei WAL.
In questo talk vorrei sottoporre la mia personale esperienza esponendo
quali sono stati i test effettuati per considerare
PostgreSQL su NFS un'opzione molto interessante, sfatando miti e
constatando fatti.
            ''',
            'speakers': [
                'Jonathan Battiato',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Postgrest: la REST API per i database PostgreSQL',
            'abstract': '''La modalita' tipica di progettazione di un sito web o applicazione mobile è la creazione di un modello di dati, la creazione di una API per la sua gestione/interazione, su cui verra' realizzato il back-end (tipicamente utilizzando un framework web)<br><br>

Vi è un nuovo paradigma di sviluppo web chiamato "noBackend". Ciò non significa eliminare completamente il back-end dalla nostra architettura, piuttosto non avere a che fare con il back-end in quanto viene creato un layer di astrazione che permette l'accesso al back-end tramite un API Javascript. Gli sviluppatori devono quindi preoccuparsi solo della user-experience. Cio' di cui si ha bisogno è una API REST, che è possibile generare automaticamente da uno schema SQL.
In questo talk, si vuole mostrare come costruire un back-end per un'applicazione web senza lasciare i confini della console PostgreSQL (beh, quasi!). Per far cio' si utilizzera' Postgrest, che converte istantaneamente lo schema in una API RESTful.<br><br>

Verranno illustrati vantaggi / limitazioni di questo approccio oltre a possibili ulteriori miglioramenti.
            ''',
            'speakers': [
                'Lucio Grenzi',
            ]
        },
        {
            'track': 'sala informatica',
            'title': 'ITPUGLab',
            'abstract': '''L'ITPUGLab è un contenitore di Open Spaces (si veda:
<a href="http://openspaceworld.org/wp2">openspaceworld.org/wp2</a>).
I partecipanti sono al centro dei vari singoli openspaces
Ognuno di loro presenta argomenti di cui vuole proporre discussione
avendo come tema fondamentale PostgreSQL, attorno ai quali si
formeranno le sessioni OST.
Le discussioni o argomenti proposti possono essere di varia natura e
non esclusivamente tecniche.
Per quelle tecniche si può far uso dei laptop che i partecipanti
saranno invitati a portare con se.
I moderatori metteranno a disposizione dei partecipanti una LAN al
fine di ottenere un ambiente condiviso attraverso cui i partecipanti
che vogliano possano anche interagire correlando le sessioni in
esperienze concrete.
La durata richiesta è di almeno due slots da 45 minuti, le passate
edizioni sono state di due ore dimostrando la durata minima ideale.
Il feedback ottenuto a fine sessione nelle precedenti edizioni
(2013-2015) ha dimostrato alto gradimento e diretta
partecipazione/coinvolgimento sfociando nella proposta di estendere la
durata della sessione all'intero pomeriggio.<br><br>

Il ruolo dei moderatori ha l'unico scopo di mantenere la pratica
dell'OST rispettata al fine di garantirne e consentirne l'efficienza
stessa.
            ''',
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
            'abstract': '''You have a system that is in production for the last four years. And this year, at the beginning of the most important event of the year, the system starts failing. Everybody starts panicking, mails start piling up, Skype rings, your phone rings and the level of induced stress can’t be measured. Between all that noises you start digging, only to see that the database is your biggest suspect. After you confirm your suspicions you are left with questions: Why? Where is the problem? How to fix it?<br><br>

This is a horror story (with twists of humour) explaining how technical debt, lack of time, ignorance, inaccurate premises, faulty hardware, and a pushy client can produce a problem that takes several hours to solve. As the plot thickens, databases failover, new contradicting elements enter the story just before the very end. (And there is another twist after the end.)
After the incident was resolved we did an extensive audit of the problematic parts of the system only to find other problems, almost all database related.<br><br>

At the end of the presentation we will show all we have learned from this experience and all the steps that should have been taken to prevent it.
            ''',
            'speakers': [
                'Mladen Marinovic',
            ]
        },
        {
            'track': 'sala conferenze',
            'title': 'Unit Test',
            'abstract': '''Quando ho cominciato a pormi il problema di fare unit test con Postgresql mi sono imbattuto in  plpgunit (https://github.com/mixerp/plpgunit/) che mi ha conquistato per la sua semplicità di installazione ed utilizzo.<br>
Il talk si propone di mettere in evidenza questo strumento, che con le modifiche apportate dal sottoscritto, si propone di avvicinare un pubblico sempre più vasto al tema del testing del database.
            ''',
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

