# -*- coding: utf-8 -*-
import sqlalchemy

def main():
  print 'attempt to connect to rds mysql db'

  db = sqlalchemy.create_engine(
    'mysql://yli:mylifeforhire@persona-testing.c9urfdd69kod.us-west-1.rds.amazonaws.com/persona_testing',
    echo=True
  )
  print 'done..'
  

if __name__ == '__main__':
  main()
