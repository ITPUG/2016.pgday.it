#!/bin/sh

cd $(dirname $0)

pelican
ghp-import -n -c 2016.pgday.it -p output
