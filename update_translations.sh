#!/bin/bash

cd awesomeconference_theme
pybabel extract --mapping babel.cfg --output messages.pot ./
pybabel update --input-file messages.pot --output-dir translations/ --domain messages
cd -
