# flaskerson

An update for my personal website (jsonbytes.com) using the python flask framework.

# database instructions:

To update database with new model or in general:
  - Get to ~/Dev/flaskerson/ in terminal
  - Put "python3" in terminal to open interactive interpreter
  - Put: from flaskblog import create_app
  - Put: create_app()

To check update went through:
  - Get to ~/Dev/flaskerson/flaskblog in terminal
  - Put "sqlite3 site.db" in terminal
  - Put: .tables

# file transfer instructions:

To transfer from local to remote (ex: images/files)
  - scp filename brunojt@45.79.14.99:/home/brunojt