# 2016pgdayIT

Questo progetto ospita il sito del PGDAY.it 2016.
Usiamo Pelican, e Python 3 come versione dell'interprete.

## Installazione

Consigliamo di creare un ambiente virtuale python e utilizzare quello
come ambiente di sviluppo.

```
$ mkvirtualenv -p python3 env_name  # se si usa virtualenvwrapper
$ virtualenv3 env_name              # se non si usa virtualenvwrapper
```

Attivare il virtualenv con

```
$ workon env_name          # se si usa virtualenvwrapper
$ . env_name/bin/activate  # se non si usa virtualenvwrapper
```

Installare le dipendenze con

```
$ pip install -r pip_requirements
```

verificare che tutto funzioni con

```
$ pelican
```

il risultato dovrebbe essere qualcosa di molto simile a

```
Done: Processed 4 articles, 0 drafts, 6 pages and 1 hidden page in 1.12 seconds.
Done: Processed 4 articles, 0 drafts, 6 pages and 1 hidden page in 2.45 seconds.
```

## Provare il sito

Per provare il sito, ci sono diversi modi, tra cui

```
cd output/ && python -m http.server
```

Consultare la documentazione ufficiale di pelican per scoprire altri metodi.

## Contribuire

### Pagine

Per modificare una pagina del sito,
aprire con un editor di testo uno dei file con estensione rst presenti nella
cartella ``content/pages`` e modificarne il contenuto.

La sintassi utilizzata e' ReStructuredText.

Una volta terminate le modifiche, generare il sito con

```
$ pelican
```


### Configurazioni avanzate

Ci sono tutta una serie di parametri che e' possibile configurare attraverso un file
di configurazione scritto in python.

Ad esempio, il programma non e' una pagina, bensi' viene generato in automatico dalla
configurazione.

I file di configurazione sono in tutto 3:

```
settings/base.py      # contiene le configurazioni generiche
settings/theme_it.py  # contiene le configurazioni per l'italiano
settings/theme_en.py  # contiene le configurazioni per l'inglese
```

Se si aprono questi file si scoprira' che i parametri sono tutti auto
esplicativi, in futuro metteremo qui una lista di tutti i parametri.

Una volta modificato un file di configurazione, rigenerare il sito con

```
$ pelican
```


### Traduzione dei template

TODO

### Contribuire sul frontend (stili css e template)

TODO

