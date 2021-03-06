# -*- coding: utf-8 -*-

from server import Note_Server
from client import Note_Client

from util import which
from util import scrubID
from util import colors

from mongo_driver import mongoDB
from sql_driver import sqliteDB

from note_printer import Note_Printer

from web import app as webapp

__author__ = 'Devin Kelly'
__email__ = 'dwwkelly@fastmail.fm'
__version__ = '0.5.2'

assert mongoDB
assert sqliteDB
assert which
assert scrubID
assert Note_Client
assert Note_Server
assert Note_Printer
assert colors
assert webapp
