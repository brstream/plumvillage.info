#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Plum Village Online Monastery Team'
SITENAME = 'Plum Village Info'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)
HIDE_DATE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PDF_GENERATOR = True
PDF_STYLE = 'fruity'
# Blogroll
LINKS =  (('Plum Village', 'http://plumvillage.org/'),
          ('The European Institute of Applied Buddhism', 'http://eiab.eu'),
          ('Wake Up', 'http://wkup.org'),)

# Social widget
SOCIAL = (('Thich Nhat Hanh on Facebook', 'http://facebook.com/thichnhathanh'),
          ('Thich Nhat Hanh on Twitter', 'http://twitter.com/thichnhathanh'),)

DEFAULT_PAGINATION = 10

THEME = 'mnmlist'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
