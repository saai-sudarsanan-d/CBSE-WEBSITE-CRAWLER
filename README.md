# CBSE-WEBSITE-CRAWLER
A program to crawl and collect data from the cbse website

The program takes as input a string of comma seperated characters assigned to the lex variable.

Paste the program into a folder and a database is created in that folder when the program runs ('cbse.db')
The Database will contain the data scraped from the cbse website after the program is done executing.

DB SCHEMA:

SRL   INT NOT NULL,

AFFL    TEXT    PRIMARY KEY    NOT NULL,

NAME    TEXT    NOT NULL,

PRNAME  TEXT    NOT NULL,

STATUS  TEXT    NOT NULL,

ADDR    CHAR(200) NOT NULL,

PHNO    TEXT,

EMAIL   TEXT,

WEBSITE TEXT
