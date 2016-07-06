# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ITPUG'
SITEURL = ''
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = u'it'
DEFAULT_DATE = 'fs'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'it': '%d/%m/%Y',
}
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_PAGES_ON_MENU = True
TYPOGRIFY = True
DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
I18N_UNTRANSLATED_ARTICLES = 'keep'
OUTPUT_PATH = 'output/'
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'minify',]
JINJA_EXTENSIONS = ['jinja2.ext.i18n',]
THEME = 'awesomeconference_theme'
PATH = 'content'
STATIC_PATHS = ['images', 'extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'}
}
MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}
HOMEPAGE_BACKGROUND_IMAGE = 'elephant.jpg'
